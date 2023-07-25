import math

HIT_RANGE = 3

class Hit_ray:
    """
    Represents a ray in a 3D world and its intersection with blocks.

    Contracts:
    - Preconditions:
        - The 'world' parameter in the constructor must be a valid World object.
        - The 'rotation' parameter in the constructor must be a tuple containing two float values (yaw and pitch) in radians.
        - The 'starting_position' parameter in the constructor must be a tuple containing three float values (x, y, z).
    - Postconditions:
        - After the constructor is called, the object's 'vector' must be a unit vector with a magnitude of 1.
        - The object's 'position' and 'block' must be initialized based on the 'starting_position'.
        - The object's 'distance' must be set to 0.

    Literate Programming:
    We will intersperse the code with explanatory comments to improve understanding.

    """

    def __init__(self, world, rotation, starting_position):
        """
        Constructor for Hit_ray.

        Parameters:
            world (World): The 3D world in which the ray exists.
            rotation (tuple): Tuple containing the rotation angles in radians (yaw, pitch).
            starting_position (tuple): Tuple containing the starting position of the ray (x, y, z).
        """
        # Check preconditions
        assert isinstance(world, World), "Invalid 'world' parameter. Expected a valid World object."
        assert isinstance(rotation, tuple) and len(rotation) == 2 and all(isinstance(angle, (int, float)) for angle in rotation), "Invalid 'rotation' parameter. Expected a tuple with two float values (yaw and pitch)."
        assert isinstance(starting_position, tuple) and len(starting_position) == 3 and all(isinstance(coord, (int, float)) for coord in starting_position), "Invalid 'starting_position' parameter. Expected a tuple with three float values (x, y, z)."

        self.world = world

        # Calculate the ray unit vector based on rotation angles
        self.vector = (
            math.cos(rotation[0]) * math.cos(rotation[1]),
            math.sin(rotation[1]),
            math.sin(rotation[0]) * math.cos(rotation[1])
        )
        
        # Initialize the ray's position and block
        self.position = list(starting_position)
        self.block = tuple(map(lambda x: int(round(x)), self.position))

        # Set the initial distance traveled by the ray
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
        # Check preconditions
        assert callable(hit_callback), "Invalid 'hit_callback' parameter. Expected a callable function."
        assert isinstance(distance, (int, float)), "Invalid 'distance' parameter. Expected a numeric value."
        assert isinstance(current_block, tuple) and len(current_block) == 3 and all(isinstance(coord, int) for coord in current_block), "Invalid 'current_block' parameter. Expected a tuple with three integer values (x, y, z)."
        assert isinstance(next_block, tuple) and len(next_block) == 3 and all(isinstance(coord, int) for coord in next_block), "Invalid 'next_block' parameter. Expected a tuple with three integer values (x, y, z)."

        if self.world.get_block_number(next_block):
            # If a block is hit, invoke the 'hit_callback' function to handle the hit
            hit_callback(current_block, next_block)
            return True
        else:
            # If no block is hit, update the ray's position and distance
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
        # Check preconditions
        assert callable(hit_callback), "Invalid 'hit_callback' parameter. Expected a callable function."

        bx, by, bz = self.block

        # Calculate the local position of the point relative to the center of the current block
        local_position = list(map(lambda x: self.position[x] - self.block[x], range(3)))

        # Determine the sign of each component of the ray vector (positive or negative)
        sign = [1, 1, 1]  # '1' for positive, '-1' for negative
        absolute_vector = list(self.vector)

        for component, element in enumerate(self.vector):
            sign[component] = 2 * (element >= 0) - 1
            absolute_vector[component] *= sign[component]
            local_position[component] *= sign[component]

        # Calculate the intersection with the +x face (fx) of the block
        if absolute_vector[0]:
            x = 0.5
            y = (0.5 - local_position[0]) / absolute_vector[0] * absolute_vector[1] + local_position[1]
            z = (0.5 - local_position[0]) / absolute_vector[0] * absolute_vector[2] + local_position[2]

            # Check if the intersection point falls within the block's face
            if y >= -0.5 and y <= 0.5 and z >= -0.5 and z <= 0.5:
                distance = math.sqrt((x - local_position[0]) ** 2 + (y - local_position[1]) ** 2 + (z - local_position[2]) ** 2)
                # Check for a potential hit with the next block in the +x direction
                return self.check(hit_callback, distance, (bx, by, bz), (bx + sign[0], by, bz))

        # Calculate the intersection with the +y face (fy) of the block
        if absolute_vector[1]:
            x = (0.5 - local_position[1]) / absolute_vector[1] * absolute_vector[0] + local_position[0]
            y = 0.5
            z = (0.5 - local_position[1]) / absolute_vector[1] * absolute_vector[2] + local_position[2]

            # Check if the intersection point falls within the block's face
            if x >= -0.5 and x <= 0.5 and z >= -0.5 and z <= 0.5:
                distance = math.sqrt((x - local_position[0]) ** 2 + (y - local_position[1]) ** 2 + (z - local_position[2]) ** 2)
                # Check for a potential hit with the next block in the +y direction
                return self.check(hit_callback, distance, (bx, by, bz), (bx, by + sign[1], bz))

        # Calculate the intersection with the +z face (fz) of the block
        if absolute_vector[2]:
            x = (0.5 - local_position[2]) / absolute_vector[2] * absolute_vector[0] + local_position[0]
            y = (0.5 - local_position[2]) / absolute_vector[2] * absolute_vector[1] + local_position[1]
            z = 0.5

            # Check if the intersection point falls within the block's face
            if x >= -0.5 and x <= 0.5 and y >= -0.5 and y <= 0.5:
                distance = math.sqrt((x - local_position[0]) ** 2 + (y - local_position[1]) ** 2 + (z - local_position[2]) ** 2)
                # Check for a potential hit with the next block in the +z direction
                return self.check(hit_callback, distance, (bx, by, bz), (bx, by, bz + sign[2]))

        # No block was hit, return False
        return False
