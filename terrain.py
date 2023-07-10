# Define the dimensions of the terrain
terrain_width = 10
terrain_height = 5
terrain_depth = 10

# Create an empty terrain
terrain = [[[None for _ in range(terrain_depth)] for _ in range(terrain_height)] for _ in range(terrain_width)]

# Function to add water blocks to the terrain
def add_water(start_x, start_y, start_z, width, height, depth):
    for x in range(start_x, start_x + width):
        for y in range(start_y, start_y + height):
            for z in range(start_z, start_z + depth):
                terrain[x][y][z] = "blue"

# Example usage: Adding water blocks to the terrain
add_water(3, 1, 3, 4, 1, 4)

# Printing the terrain
for y in range(terrain_height):
    for z in range(terrain_depth):
        for x in range(terrain_width):
            block = terrain[x][y][z]
            if block is None:
                print("  ", end="")
            else:
                print(block + " ", end="")
        print()
    print()

import unittest

# Function to create an empty terrain
def create_empty_terrain(width, height, depth):
    return [[[None for _ in range(depth)] for _ in range(height)] for _ in range(width)]
    
# Function to add water blocks to the terrain using specified coordinates and dimensions
def add_water(terrain, start_x, start_y, start_z, width, height, depth):
    for x in range(start_x, start_x + width):
        for y in range(start_y, start_y + height):
            for z in range(start_z, start_z + depth):
                terrain[x][y][z] = "blue"
                
# Function to print the terrain
def print_terrain(terrain):
    for y in range(len(terrain[0])):
        for z in range(len(terrain[0][0])):
            for x in range(len(terrain)):
                block = terrain[x][y][z]
                if block is None:
                    print("  ", end="")
                else:
                    print(block + " ", end="")
            print()
        print()

'''Testing if any errors in funtion print_terrain, allows for full automated testing and code coverage'''
def test_print():
    try:
        print_terrain(terrain)
        assert(True)
    except:
        assert(False)

class TestTerrain(unittest.TestCase):
     # Define the dimensions of the terrain for unit testing
    def setUp(self):
        self.terrain_width = 10
        self.terrain_height = 5
        self.terrain_depth = 10
        self.terrain = create_empty_terrain(self.terrain_width, self.terrain_height, self.terrain_depth)

    def test_add_water_single_block(self):
         # Test adding a single water block to the terrain
        add_water(self.terrain, 3, 1, 3, 1, 1, 1)
        self.assertEqual(self.terrain[3][1][3], "blue")

    def test_add_water_multiple_blocks(self):
        # Test adding multiple water blocks to the terrain
        add_water(self.terrain, 2, 0, 2, 3, 3, 3)
        for x in range(2, 5):
            for y in range(0, 3):
                for z in range(2, 5):
                    self.assertEqual(self.terrain[x][y][z], "blue")
