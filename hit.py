import math

HIT_RANGE = 3

class Hit_ray:
    """
    Represents a ray in a 3D world and its intersection with blocks.
    """

    def __init__(self, world, rotation, starting_position):
        """
        Constructor for Hit_ray.

        Parameters:
            world (World): The 3D world in which the ray exists.
            rotation (tuple): Tuple containing the rotation angles in radians (yaw, pitch).
            starting_position (tuple): Tuple containing the starting position of the ray (x, y, z).
        """
        self.world = world

        # Get the ray unit vector based on rotation angles
        # sqrt(ux ^ 2 + uy ^ 2 + uz ^ 2) must always equal 1
        self.vector = (
            math.cos(rotation[0]) * math.cos(rotation[1]),
            math.sin(rotation[1]),
            math.sin(rotation[0]) * math.cos(rotation[1])
        )
        
        # Point position where the ray is currently located
        self.position = list(starting_position)

        # Block position in which the point currently resides
        self.block = tuple(map(lambda x: int(round(x)), self.position))

        # Current distance the point has traveled along the ray
        self.distance = 0

    def check(self, hit_callback, distance, current_block, next_block):
        """
        Check for a potential hit with a block along the ray path.

        Parameters:
            hit_callback (function): A callback function to be called when a block is hit.
            distance (float): The distance traveled from the current point to the next point.
            current_block (tuple): Tuple containing the current block's position (x, y, z).
            next_block (tuple): Tuple containing the next block's position (x, y, z).

        Returns:
            bool: True if a block is hit, False otherwise.
        """
        if self.world.get_block_number(next_block):
            hit_callback(current_block, next_block)
            return True
        else:
            self.position = list(map(lambda x: self.position[x] + self.vector[x] * distance, range(3)))
            self.block = next_block
            self.distance += distance
            return False

    def step(self, hit_callback):
        """
        Move the ray one step forward and check for intersections with blocks.

        Parameters:
            hit_callback (function): A callback function to be called when a block is hit.

        Returns:
            bool: True if a block is hit, False otherwise.
        """
        bx, by, bz = self.block

        # Point position relative to block center
        local_position = list(map(lambda x: self.position[x] - self.block[x], range(3)))

        # Determine which components of the ray vector are positive or negative
        sign = [1, 1, 1]  # '1' for positive, '-1' for negative
        absolute_vector = list(self.vector)

        for component, element in enumerate(self.vector):
            sign[component] = 2 * (element >= 0) - 1
            absolute_vector[component] *= sign[component]
            local_position[component] *= sign[component]

        lx, ly, lz = local_position
        vx, vy, vz = absolute_vector

        # Intersection with +x face (fx)
        if vx:
            x = 0.5
            y = (0.5 - lx) / vx * vy + ly
            z = (0.5 - lx) / vx * vz + lz

            if y >= -0.5 and y <= 0.5 and z >= -0.5 and z <= 0.5:
                distance = math.sqrt((x - lx) ** 2 + (y - ly) ** 2 + (z - lz) ** 2)
                return self.check(hit_callback, distance, (bx, by, bz), (bx + sign[0], by, bz))

        # Intersection with +y face (fy)
        if vy:
            x = (0.5 - ly) / vy * vx + lx
            y = 0.5
            z = (0.5 - ly) / vy * vz + lz

            if x >= -0.5 and x <= 0.5 and z >= -0.5 and z <= 0.5:
                distance = math.sqrt((x - lx) ** 2 + (y - ly) ** 2 + (z - lz) ** 2)
                return self.check(hit_callback, distance, (bx, by, bz), (bx, by + sign[1], bz))

        # Intersection with +z face (fz)
        if vz:
            x = (0.5 - lz) / vz * vx + lx
            y = (0.5 - lz) / vz * vy + ly
            z = 0.5

            if x >= -0.5 and x <= 0.5 and y >= -0.5 and y <= 0.5:
                distance = math.sqrt((x - lx) ** 2 + (y - ly) ** 2 + (z - lz) ** 2)
                return self.check(hit_callback, distance, (bx, by, bz), (bx, by, bz + sign[2]))
