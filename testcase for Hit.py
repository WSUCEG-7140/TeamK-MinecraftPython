import unittest
import math

# World class for testing purposes
class World:
    def __init__(self):
        self.blocks = {}  # Dictionary to store block positions and block numbers

    def add_block(self, position, block_number):
        self.blocks[position] = block_number

    def get_block_number(self, position):
        return self.blocks.get(position, 0)  # Returns 0 if no block exists at the position


class TestHitRay(unittest.TestCase):

    def setUp(self):
        # Create a simple world with appropriate blocks for testing
        self.world = World()
        self.world.add_block((1, 0, 0), 1)  # Add a block with block number 1 at position (1, 0, 0)
        self.world.add_block((1, 1, 1), 2)  # Add a block with block number 2 at position (1, 1, 1)
        self.world.add_block((2, 0, 0), 3)  # Add a block with block number 3 at position (2, 0, 0)

    def test_basic_intersection(self):
        # Create a ray starting at (0, 0, 0) and moving in the +x direction
        ray = Hit_ray(self.world, (0, 0), (0, 0, 0))

        # Step the ray to check for intersection with the block
        result = ray.step(lambda current_block, next_block: None)

        # The ray should hit the block at (1, 0, 0), so the result should be True
        self.assertTrue(result)

    def test_no_intersection(self):
        # Create a ray starting at (0, 0, 0) and moving in the -x direction
        ray = Hit_ray(self.world, (math.pi, 0), (0, 0, 0))

        # Step the ray to check for intersection with the block
        result = ray.step(lambda current_block, next_block: None)

        # The ray should not hit any block, so the result should be False
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

"""
expected output:
ran testcases in 0.01 seconds

"""
