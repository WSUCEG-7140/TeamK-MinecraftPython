"""
Tests from terrain.py
"""

import unittest

# Define the dimensions of the terrain
terrain_width = 10
terrain_height = 5
terrain_depth = 10

# Create an empty terrain
terrain = [[[None for _ in range(terrain_depth)] for _ in range(terrain_height)] for _ in range(terrain_width)]

# Function to add water blocks to the terrain
def add_water(start_x, start_y, start_z, width, height, depth):
    """
    Add water blocks to the terrain within the specified coordinates and dimensions.

    @param start_x (int): The starting x-coordinate.
    @param start_y (int): The starting y-coordinate.
    @param start_z (int): The starting z-coordinate.
    @param width (int): The width of the water area.
    @param height (int): The height of the water area.
    @param depth (int): The depth of the water area.
    """
    for x in range(start_x, start_x + width):
        for y in range(start_y, start_y + height):
            for z in range(start_z, start_z + depth):
                terrain[x][y][z] = "blue"

# Example usage: Adding water blocks to the terrain
add_water(3, 1, 3, 4, 1, 4)

# Define a test case for adding water
class TestAddWater(unittest.TestCase):
    def test_water_added_correctly(self):
        # Check if water blocks are added correctly to the terrain
        for x in range(terrain_width):
            for y in range(terrain_height):
                for z in range(terrain_depth):
                    if x >= 3 and x <= 6 and y == 1 and z >= 3 and z <= 6:
                        # Expected: "blue" in the specified area
                        self.assertEqual(terrain[x][y][z], "blue")
                    else:
                        # Expected: None in the rest of the terrain
                        self.assertIsNone(terrain[x][y][z])
                        
                        
if __name__ == '__main__':
    unittest.main()

"""
 Expected Output:                                     
          blue blue blue        
          blue blue blue        
          blue blue blue  

ran testcase in 0.01
ok
"""
