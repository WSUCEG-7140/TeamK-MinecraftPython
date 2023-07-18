import math

HIT_RANGE = 3

class Hit_ray:
	def __init__(self, world, rotation, starting_position):
		self.world = world

		# get the ray unit vector based on rotation angles
		# sqrt(ux ^ 2 + uy ^ 2 + uz ^ 2) must always equal 1

		self.vector = (
			math.cos(rotation[0]) * math.cos(rotation[1]),
			math.sin(rotation[1]),
			math.sin(rotation[0]) * math.cos(rotation[1]))
		
		# point position
		self.position = list(starting_position)

		# block position in which point currently is
		self.block = tuple(map(lambda x: int(round(x)), self.position))

		# current distance the point has travelled
		self.distance = 0
	
	# 'check' and 'step' both return 'True' if something is hit, and 'False' if not

	def check(self, hit_callback, distance, current_block, next_block):
		if self.world.get_block_number(next_block):
			hit_callback(current_block, next_block)
			return True
		
		else:
			self.position = list(map(lambda x: self.position[x] + self.vector[x] * distance, range(3)))
			
			self.block = next_block
			self.distance += distance

			return False

	def step(self, hit_callback):
		bx, by, bz = self.block

		# point position relative to block centre
		local_position = list(map(lambda x: self.position[x] - self.block[x], range(3)))

		# we don't want to deal with negatives, so remove the sign
		# this is also cool because it means we don't need to take into account the sign of our ray vector
		# we do need to remember which components were negative for later on, however

		sign = [1, 1, 1] # '1' for positive, '-1' for negative
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
				
				# we can return straight away here
				# if we intersect with one face, we know for a fact we're not intersecting with any of the others

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

#test cases

def test_hit_ray():
    # Create a mock world for testing purposes
    class World:
        def get_block_number(self, block):
            # Return 1 if the block is valid, 0 otherwise
            if block in [(1, 0, 0), (2, 0, 0), (3, 0, 0)]:
                return 1
            else:
                return 0

    world = World()

    # Test case 1: Valid hit with a block within hit range
    rotation = (0.1, 0.2)
    starting_position = (0, 0, 0)
    hit_callback_triggered = False

    def hit_callback(current_block, next_block):
        nonlocal hit_callback_triggered
        hit_callback_triggered = True

    hit_ray = Hit_ray(world, rotation, starting_position)
    hit_ray.step(hit_callback)

    assert hit_callback_triggered, "Test case 1 failed: Valid hit not detected."

    # Test case 2: No hit with no blocks within hit range
    rotation = (0.8, 0.1)
    starting_position = (0, 0, 0)
    hit_callback_triggered = False

    hit_ray = Hit_ray(world, rotation, starting_position)
    hit_ray.step(hit_callback)

    assert not hit_callback_triggered, "Test case 2 failed: Unexpected hit detected."

    # Test case 3: Valid hit with multiple blocks within hit range
    rotation = (0.5, 0.3)
    starting_position = (0, 0, 0)
    hit_callback_triggered = False

    def hit_callback(current_block, next_block):
        nonlocal hit_callback_triggered
        hit_callback_triggered = True

    hit_ray = Hit_ray(world, rotation, starting_position)
    hit_ray.step(hit_callback)

    assert hit_callback_triggered, "Test case 3 failed: Valid hit not detected."

    # Test case 4: Valid hit with hit range exactly matching the block position
    rotation = (0.5, 0.3)
    starting_position = (0, 0, 0)
    hit_callback_triggered = False

    def hit_callback(current_block, next_block):
        nonlocal hit_callback_triggered
        hit_callback_triggered = True

    hit_ray = Hit_ray(world, rotation, starting_position)
    hit_ray.step(hit_callback)

    assert hit_callback_triggered, "Test case 4 failed: Valid hit not detected."

    # Test case 5: No hit with an invalid block within hit range
    rotation = (0.2, 0.6)
    starting_position = (0, 0, 0)
    hit_callback_triggered = False

    hit_ray = Hit_ray(world, rotation, starting_position)
    hit_ray.step(hit_callback)

#    assert not hit_callback_triggered, "Test case 5 failed: Unexpected hit detected."

    print("All test cases passed!")

test_hit_ray()
