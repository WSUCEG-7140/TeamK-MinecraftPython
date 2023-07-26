"""
Tests from terrain.py
"""
import unittest

class TestTerrain(unittest.TestCase):
    """
    Test case for the terrain functions.
    """

    def test_add_water_single_block(self):
        """
        Test adding a single water block to the terrain.
        """
        terrain = create_empty_terrain(10, 5, 10)
        add_water(terrain, 3, 1, 3, 1, 1, 1)
        self.assertEqual(terrain[3][1][3], "blue")

    def test_add_water_multiple_blocks(self):
        """
        Test adding multiple water blocks to the terrain.
        """
        terrain = create_empty_terrain(10, 5, 10)
        add_water(terrain, 2, 0, 2, 3, 3, 3)
        for x in range(2, 5):
            for y in range(0, 3):
                for z in range(2, 5):
                    self.assertEqual(terrain[x][y][z], "blue")

    def test_print_terrain(self):
        """
        Test printing the terrain.
        """
        terrain = create_empty_terrain(10, 5, 10)
        # Add some water to the terrain
        add_water(terrain, 2, 0, 2, 3, 3, 3)
        try:
            # Capture the printed output using StringIO
            from io import StringIO
            import sys

            captured_output = StringIO()
            sys.stdout = captured_output

            # Call the function that prints the terrain
            print_terrain(terrain)

            # Reset stdout
            sys.stdout = sys.__stdout__

            # Validate the printed output
            expected_output = (
                "        \n"
                "        \n"
                "        \n"
                "  blue blue blue     \n"
                "  blue blue blue     \n"
                "  blue blue blue     \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
            )
            self.assertEqual(captured_output.getvalue(), expected_output)
        except Exception as e:
            self.fail(f"Printing the terrain failed with exception: {e}")

# Function to create an empty terrain
def create_empty_terrain(width, height, depth):
    """
    Create an empty terrain with the specified dimensions.

    Args:
        width (int): The width of the terrain.
        height (int): The height of the terrain.
        depth (int): The depth of the terrain.

    Returns:
        list: The empty terrain as a 3D list.

    """
    return [[[None for _ in range(depth)] for _ in range(height)] for _ in range(width)]

# Function to add water blocks to the terrain using specified coordinates and dimensions
def add_water(terrain, start_x, start_y, start_z, width, height, depth):
    """
    Add water blocks to the terrain within the specified coordinates and dimensions.

    Args:
        terrain (list): The terrain to modify.
        start_x (int): The starting x-coordinate.
        start_y (int): The starting y-coordinate.
        start_z (int): The starting z-coordinate.
        width (int): The width of the water area.
        height (int): The height of the water area.
        depth (int): The depth of the water area.

    """
    for x in range(start_x, start_x + width):
        for y in range(start_y, start_y + height):
            for z in range(start_z, start_z + depth):
                terrain[x][y][z] = "blue"

# Function to print the terrain
def print_terrain(terrain):
    """
    Print the terrain.

    Args:
        terrain (list): The terrain to print.

    """
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

class TestTerrain(unittest.TestCase):
    """
    Test case for the terrain functions.
    """

    def test_add_water_single_block(self):
        """
        Test adding a single water block to the terrain.
        """
        terrain = create_empty_terrain(10, 5, 10)
        add_water(terrain, 3, 1, 3, 1, 1, 1)
        self.assertEqual(terrain[3][1][3], "blue")

    def test_add_water_multiple_blocks(self):
        """
        Test adding multiple water blocks to the terrain.
        """
        terrain = create_empty_terrain(10, 5, 10)
        add_water(terrain, 2, 0, 2, 3, 3, 3)
        for x in range(2, 5):
            for y in range(0, 3):
                for z in range(2, 5):
                    self.assertEqual(terrain[x][y][z], "blue")

    def test_print_terrain(self):
        """
        Test printing the terrain.
        """
        terrain = create_empty_terrain(10, 5, 10)
        try:
            print_terrain(terrain)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
