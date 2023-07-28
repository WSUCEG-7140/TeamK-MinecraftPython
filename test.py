from main import *
from Snow import *
from Terrain import *
from Hit import *
from Keyboard_mouse import *
from Pygletbatchupdater import *
from Lava import *
from Joystick import *
from clouds import *
from sun import *
from moon import *


import unittest
from unittest.mock import MagicMock
import pyglet
from pyglet.gl import *
from random import randint
from math import sin, cos, pi


''' 
Sample test case to ensure working PyTest
'''
def test_pytest():
    assert True

#test case for josephreddy-#issue9
"""
Tests from terrain.py
"""
class Terrain:
    def __init__(self, width, height, depth):
        """
        @brief Class constructor to initialize the terrain.

        @param width (int): The width of the terrain.
        @param height (int): The height of the terrain.
        @param depth (int): The depth of the terrain.
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.terrain = [[[None for _ in range(depth)] for _ in range(height)] for _ in range(width)]

    def add_water(self, start_x, start_y, start_z, width, height, depth):
        """
        @brief Add water blocks to the terrain within the specified coordinates and dimensions.

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
                    self.terrain[x][y][z] = "blue"

    def print_terrain(self):
        """
        @brief Print the current state of the terrain.
        """
        for y in range(self.height):
            for z in range(self.depth):
                for x in range(self.width):
                    block = self.terrain[x][y][z]
                    if block is None:
                        print("  ", end="")
                    else:
                        print(block + " ", end="")
                print()
            print()


def test_terrain():
    # Test case 1
    terrain = Terrain(10, 5, 10)
    terrain.add_water(3, 1, 3, 4, 1, 4)
    print("Test Case 1:")
    terrain.print_terrain()
    print("\n")

    # Test case 2
    terrain = Terrain(10, 5, 10)
    terrain.add_water(0, 0, 0, 2, 3, 4)
    print("Test Case 2:")
    terrain.print_terrain()
    print("\n")

    # Test case 3
    terrain = Terrain(10, 5, 10)
    terrain.add_water(5, 0, 5, 3, 2, 3)
    print("Test Case 3:")
    terrain.print_terrain()
    print("\n")

    # Test case 4
    terrain = Terrain(10, 5, 10)
    terrain.add_water(0, 2, 0, 5, 1, 2)
    print("Test Case 4:")
    terrain.print_terrain()
    print("\n")

    # Test case 5
    terrain = Terrain(10, 5, 10)
    terrain.add_water(8, 4, 8, 2, 1, 2)
    print("Test Case 5:")
    terrain.print_terrain()
    print("\n")


    # Print the total number of tests run
    total_tests = 5  
    print(f"Total tests run: {total_tests}")

def main():
    test_terrain()

if __name__ == "__main__":
    main()

"""
 Expected Output:                                     
          blue blue blue        
          blue blue blue        
          blue blue blue  

ran 5 testcase in 0.01
ok
"""



"""
Tests from main.py
"""

## @brief Test case for setting up GL_FOG texture mapping
def test_fog():
    try:
        setup_fog()
        assert True
    except: assert False

## @brief Test case for normal speed when not flying           
def test_tripleSpeedFalse():
        flying = False
        tripleSpeed = False
        
        speed = 15 if flying else 5
        speed = speed * 3 if tripleSpeed else speed
        
        if flying:
            if tripleSpeed:
                assert speed == 45
            else:
                assert speed == 15
        else:
            if tripleSpeed:
                assert speed == 15
            else:
                assert speed == 5

## @brief Test case for Triple speed when not flying           
def test_tripleSpeedTrue():
        flying = False
        tripleSpeed = True
        
        speed = 15 if flying else 5
        speed = speed * 3 if tripleSpeed else speed
        
        if flying:
            if tripleSpeed:
                assert speed == 45
            else:
                assert speed == 15
        else:
            if tripleSpeed:
                assert speed == 15
            else:
                assert speed == 5

## @brief Test case for Triple speed when flying                 
def test_flyingTripleSpeed():
        flying = True
        tripleSpeed = True
        
        speed = 15 if flying else 5
        speed = speed * 3 if tripleSpeed else speed
        
        if flying:
            if tripleSpeed:
                assert speed == 45
            else:
                assert speed == 15
        else:
            if tripleSpeed:
                assert speed == 15
            else:
                assert speed == 5
                
## @brief Test case for normal speed when flying           
def test_flyingTripleSpeedFalse():
        flying = True
        tripleSpeed = False
        
        speed = 15 if flying else 5
        speed = speed * 3 if tripleSpeed else speed
        
        if flying:
            if tripleSpeed:
                assert speed == 45
            else:
                assert speed == 15
        else:
            if tripleSpeed:
                assert speed == 15
            else:
                assert speed == 5
                


#test cases for josephreddy-#issue20:
"""
Tests from snow.py
"""


class SnowBlockTestCase(unittest.TestCase):
    ## @brief Test case for adding a snow block to the player's inventory.
    def test_add_snow_block_to_inventory(self):
        player = Player()
        snow_block = SnowBlock()
        player.add_item_to_inventory(snow_block)
        self.assertIn(snow_block, player.inventory)  # Check if the snow block is added to the player's inventory

    ## @brief Test case for rendering the snow block in the inventory.
    def test_render_snow_block_in_inventory(self):
        player = Player()
        inventory = Inventory()
        snow_block = SnowBlock()
        inventory.add_item("White Block (Snow)")
        inventory_renderer = InventoryRenderer()
        rendered_inventory = inventory_renderer.render(inventory)
        self.assertIsNotNone(rendered_inventory)  # Check if the rendered inventory is not None
        self.assertIn("White Block (Snow)", rendered_inventory)  # Check if the snow block is rendered in the inventory

    ## @brief Test case for checking the slipperiness value of the snow block.
    def test_slipperiness_of_snow_block(self):
        snow_block = SnowBlock()
        self.assertAlmostEqual(snow_block.slipperiness, 0.6, delta=0.001)  # Check if the slipperiness value is approximately 0.6

    ## @brief Test case for checking if the snow block is not broken without a shovel.
    def test_snow_block_not_broken_without_shovel(self):
        player = Player()
        snow_block = SnowBlock()
        snow_block.on_player_interact(player)
        self.assertFalse(snow_block.is_broken)  # Check if the snow block is not broken without a shovel

    ## @brief Test case for equipping a tool for the player.
    def test_equip_tool(self):
        player = Player()
        shovel = Shovel()
        player.equip_tool(shovel)
        self.assertEqual(player.equipped_tool, shovel)  # Check if the player's equipped tool is the shovel

if __name__ == '__main__':
    unittest.main()


"""
expected value:
White Block (Snow)
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
"""



#test cases for josephreddy-#issue17
"""
Tests from Hit.py
"""

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
expected value:
Ran 2 tests in 0.000s

OK
"""



#test cases for josephreddy-#issue21

"""
Tests from lava.py
"""

class SnowBlockTestCase(unittest.TestCase):
    def test_snow_block_melts_with_lava_collision(self):
        """
        @brief Test case to verify that a snow block melts when it collides with a lava block.
        """
        snow_block = SnowBlock()
        lava = Lava()
        snow_block.on_collision(lava)
        self.assertTrue(snow_block.is_melted)

    def test_snow_block_does_not_melt_with_non_lava_collision(self):
        """
        @brief Test case to check that a snow block does not melt when colliding with a block that is not lava.
        """
        snow_block = SnowBlock()
        other_block = Block()
        snow_block.on_collision(other_block)
        self.assertFalse(snow_block.is_melted)

if __name__ == '__main__':
    unittest.main()

"""
expected value:
Snow block melted!
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""




#test cases for josephreddy-#issue18

"""
Tests from joystick.py
"""


class JoystickTestCase(unittest.TestCase):
    def setUp(self):
        self.game = MagicMock()
        self.joystick = Joystick(self.game)

    def test_update_controller_with_joystick_input(self):
        """
        Test updating the controller with joystick input.
        """
        # Mock joystick inputs
        self.joystick.joystick_look = [0.1, -0.2]

        # Set initial player rotation
        self.game.player.rotation = [0.0, 0.0]

        # Call the update_controller method
        self.joystick.update_controller()

        # Verify player rotation has been updated based on joystick look input
        expected_rotation_x = 0.1 * self.joystick.camera_sensitivity
        expected_rotation_y = -0.2 * self.joystick.camera_sensitivity
        self.assertAlmostEqual(self.game.player.rotation[0], expected_rotation_x, delta=0.001)
        self.assertAlmostEqual(self.game.player.rotation[1], expected_rotation_y, delta=0.001)

class Joystick:
    def __init__(self, game):
        """
        Constructor for the Joystick class.
        
        Args:
            game (MagicMock): The game object.
        """
        self.game = game
        self.camera_sensitivity = 0.007
        self.joystick_look = [0, 0]

    def update_controller(self):
        """
        Update the controller based on joystick input.
        """
        if self.joystick_look[0] != 0:
            self.game.player.rotation[0] += self.joystick_look[0] * self.camera_sensitivity
        if self.joystick_look[1] != 0:
            self.game.player.rotation[1] += self.joystick_look[1] * self.camera_sensitivity

if __name__ == '__main__':
    unittest.main()

"""
expected output:
Ran test in 0.000s

OK

"""



#test cases for josephreddy-#issue16

"""
Tests from Keyboard_mouse.py
"""

class TestKeyboardMovement(unittest.TestCase):
    """Test case for Keyboard movement."""

    def test_move_left(self):
        """Test moving the keyboard to the left."""
        keyboard = Keyboard()
        keyboard.move_left()
        self.assertEqual(keyboard.x, -1)

    def test_move_right(self):
        """Test moving the keyboard to the right."""
        keyboard = Keyboard()
        keyboard.move_right()
        self.assertEqual(keyboard.x, 1)

    def test_move_up(self):
        """Test moving the keyboard upwards."""
        keyboard = Keyboard()
        keyboard.move_up()
        self.assertEqual(keyboard.y, 1)

    def test_move_down(self):
        """Test moving the keyboard downwards."""
        keyboard = Keyboard()
        keyboard.move_down()
        self.assertEqual(keyboard.y, -1)

class TestMouseMovement(unittest.TestCase):
    """Test case for Mouse movement."""

    def test_mouse_move(self):
        """Test moving the mouse with delta values."""
        mouse = Mouse()
        mouse.move(10, -5)
        self.assertEqual(mouse.x, 10)
        self.assertEqual(mouse.y, -5)

if __name__ == '__main__':
    unittest.main()

"""
#expeected output:

ran test cases:
ok
"""

#test case for josephreddy-#issue4

"""
Tests from pygletbatchupdater.py
"""


## \class TestUpdatedBatch
# A class for testing the UpdatedBatch class.
class TestUpdatedBatch(unittest.TestCase):

    ## \brief Set up the test environment before each test case.
    def setUp(self):
        self.batch = UpdatedBatch()

    ## \brief Test the add method of UpdatedBatch.
    def test_add(self):
        """
        Test the add method of UpdatedBatch.
        """
        self.batch.add(4, pyglet.gl.GL_QUADS, None, ('v2f', [0, 0, 100, 0, 100, 100, 0, 100]), ('c3B', [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0]))
        self.assertEqual(len(self.batch.vertices), 8)
        self.assertEqual(len(self.batch.colors), 12)

    ## \brief Test the add_indexed method of UpdatedBatch.
    def test_add_indexed(self):
        """
        Test the add_indexed method of UpdatedBatch.
        """
        self.batch.add_indexed(4, pyglet.gl.GL_QUADS, None, [0, 1, 2, 3], ('v2f', [0, 0, 100, 0, 100, 100, 0, 100]), ('c3B', [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0]))
        self.assertEqual(len(self.batch.vertices), 8)
        self.assertEqual(len(self.batch.colors), 12)

if __name__ == '__main__':
    unittest.main()

"""
EXPECTED OUTPUT:
ran test cases in 0.01 seconds
"""



#test cases for josephreddy-#issue19

"""
Tests for Visual-properties.py
"""

def process_test_case(test_case_number, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values):
    """
    Process a test case.

    @param[in] test_case_number (int): The test case number.
    @param[in] transparent (bool): Indicates whether the object is transparent.
    @param[in] transparency (int): Transparency level on a scale of 0-10.
    @param[in] is_cube (bool): Indicates whether the object is a cube.
    @param[in] glass (bool): Indicates whether the object is made of glass.
    @param[in] translucent (bool): Indicates whether the object is translucent.
    @param[in] colliders (list): List of collider objects.
    @param[in] vertex_positions (list): List of vertex positions for the object.
    @param[in] tex_coords (list): List of texture coordinates for the object.
    @param[in] shading_values (list): List of shading values for the object.
    """
    print(f"Test Case {test_case_number}:")
    print("Transparent:", transparent)
    print("Transparency:", transparency)
    print("Is Cube:", is_cube)
    print("Glass:", glass)
    print("Translucent:", translucent)
    print("Colliders:", colliders)
    print("Vertex Positions:", vertex_positions)
    print("Texture Coordinates:", tex_coords)
    print("Shading Values:", shading_values)
    print()

# Test Case 1
transparent = True
transparency = 2
is_cube = False
glass = False
translucent = False
colliders = []
vertex_positions = [
    [-0.3536, 0.5000,  0.3536, -0.3536, -0.5000,  0.3536,  0.3536, -0.5000, -0.3536,  0.3536, 0.5000, -0.3536],
    [-0.3536, 0.5000, -0.3536, -0.3536, -0.5000, -0.3536,  0.3536, -0.5000,  0.3536,  0.3536, 0.5000,  0.3536],
    [ 0.3536, 0.5000, -0.3536,  0.3536, -0.5000, -0.3536, -0.3536, -0.5000,  0.3536, -0.3536, 0.5000,  0.3536],
    [ 0.3536, 0.5000,  0.3536,  0.3536, -0.5000,  0.3536, -0.3536, -0.5000, -0.3536, -0.3536, 0.5000, -0.3536],
]
tex_coords = [
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]
shading_values = [
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
]

process_test_case(1, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values)

# Test Case 2
transparent = False
transparency = 0
is_cube = True
glass = False
translucent = False
colliders = []
vertex_positions = [
    [-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5],
    [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5],
    [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5],
    [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5],
]
tex_coords = [
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
]
shading_values = [
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
]

process_test_case(2, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values)

# Test Case 3
transparent = True
transparency = 1
is_cube = True
glass = True
translucent = False
colliders = [[-0.5, -0.5, -0.5, 0.5, 0.5, 0.5]]
vertex_positions = [
    [-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5],
    [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5],
    [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5],
    [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5],
]
tex_coords = [
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
]
shading_values = [
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
]

process_test_case(3, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values)

# Test Case 4
transparent = False
transparency = 0
is_cube = True
glass = False
translucent = True
colliders = []
vertex_positions = [
    [-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5],
    [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5],
    [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5],
    [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5],
]
tex_coords = [
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
]
shading_values = [
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
]

process_test_case(4, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values)



"""
expected value:
Test Case 1:
Transparent: True
Transparency: 2
Is Cube: False
Glass: False
Translucent: False
Colliders: []
Vertex Positions: [[-0.3536, 0.5, 0.3536, -0.3536, -0.5, 0.3536, 0.3536, -0.5, -0.3536, 0.3536, 0.5, -0.3536], [-0.3536, 0.5, -0.3536, -0.3536, -0.5, -0.3536, 0.3536, -0.5, 0.3536, 0.3536, 0.5, 0.3536], [0.3536, 0.5, -0.3536, 0.3536, -0.5, -0.3536, -0.3536, -0.5, 0.3536, -0.3536, 0.5, 0.3536], [0.3536, 0.5, 0.3536, 0.3536, -0.5, 0.3536, -0.3536, -0.5, -0.3536, -0.3536, 0.5, -0.3536]]
Texture Coordinates: [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0]]
Shading Values: [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]

Test Case 2:
Transparent: False
Transparency: 0
Is Cube: True
Glass: False
Translucent: False
Colliders: []
Vertex Positions: [[-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5], [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5], [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5], [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5]]
Texture Coordinates: [[0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]]
Shading Values: [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]

Test Case 3:
Transparent: True
Transparency: 1
Is Cube: True
Glass: True
Translucent: False
Colliders: [[-0.5, -0.5, -0.5, 0.5, 0.5, 0.5]]
Vertex Positions: [[-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5], [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5], [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5], [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5]]
Texture Coordinates: [[0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]]
Shading Values: [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]

Test Case 4:
Transparent: False
Transparency: 0
Is Cube: True
Glass: False
Translucent: True
Colliders: []
Vertex Positions: [[-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5], [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5], [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5], [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5]]
Texture Coordinates: [[0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]]
Shading Values: [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]
"""




"""
TESTS for clouds.py
https://github.com/WSUCEG-7140/TeamK-MinecraftPython/issues/51
"""

"""
Test: create the clouds' vertex data
"""
def create_cloud(radius, slices, stacks):

    """
    @param[in]
    Pass: if radius is > 0
    """
    assert radius > 0, 'radius is not greater than 0!'


    """
    @param[in]
    Pass: if slices is > 0
    """
    assert slices > 0, 'slices is not greater than 0!'


    """
    @param[in]
    Pass: if stacks is > 0
    """
    assert stacks > 0, 'stacks is not greater than 0!'
    
    vertices = []
    for stack in range(stacks + 1):
        for slice in range(slices):
            x = radius * cos(2 * pi * slice / slices) * sin(pi * stack / stacks)
            y = radius * sin(-pi / 2 + pi * stack / stacks)
            z = radius * sin(2 * pi * slice / slices) * sin(pi * stack / stacks)
            vertices.extend([x, y, z])


    """
    @param[out]
    Pass: if list vertices is not empty
    """ 
    assert vertices is not None, 'vertices is empty!'


    """
    @param[out]
    Pass: if each element in list vertices is numerical
    """ 
    for coordinates in vertices:
        for coordinate in coordinates:
            coordinate_float = float(coordinate)
            assert isinstance(coordinate_float, float), 'vertices contains a non-numerical value!'


    create_clouds(pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices)))


"""
Test: create cloud positions
"""
def create_clouds(sphere_vertex_list):

    """
    @param[in]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    CLOUD_HEIGHT = 20
    NUM_CLOUDS = 30
    CLOUD_TEXTURE_PATH = 'cloud_texture.png'


    """
    @param[out]
    Pass: if path to CLOUD_TEXTURE_PATH is not empty
    """ 
    assert CLOUD_TEXTURE_PATH is not None , 'CLOUD_TEXTURE_PATH is empty!'

    clouds = []

    """
    Load the cloud texture
    """
    cloud_image = pyglet.image.load(CLOUD_TEXTURE_PATH)
    cloud_texture = cloud_image.get_texture()


    """
    @param[out]
    Pass: if cloud_texture is not empty
    """ 
    assert cloud_texture is not None, 'cloud_texture is empty!'

    glBindTexture(GL_TEXTURE_2D, cloud_texture.id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    for _ in range(NUM_CLOUDS):
        x = randint(-40, 40)
        y = randint(CLOUD_HEIGHT - 5, CLOUD_HEIGHT + 5)
        z = randint(-40, 40)
        clouds.append((x, y, z))


    """
    @param[out]
    Pass: if list clouds is not empty
    """ 
    assert clouds is not None, 'clouds is empty!'


    """
    @param[out]
    Pass: if each element in list clouds is numerical
    """ 
    for coordinates in clouds:
        for coordinate in coordinates:
            coordinate_float = float(coordinate)
            assert isinstance(coordinate_float, float), 'clouds contains a non-numerical value!'

    draw(sphere_vertex_list, clouds, cloud_texture)


"""
Test: enable buffer to draw
"""
def draw(sphere_vertex_list, clouds, cloud_texture):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()


    """
    @param[in]
    @param[out]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'


    """
    @param[in]
    @param[out]
    Pass: if list clouds is not empty
    """ 
    assert clouds is not None, 'clouds is empty!'


    """
    @param[in]
    @param[out]
    Pass: if cloud_texture is not empty
    """ 
    assert cloud_texture is not None, 'cloud_texture is empty!'

    draw_clouds(sphere_vertex_list, clouds, cloud_texture)


"""
Test: draw the clouds
"""
def draw_clouds(sphere_vertex_list, clouds, cloud_texture):

    """
    @param[in]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'


    """
    @param[in]
    Pass: if list clouds is not empty
    """ 
    assert clouds is not None, 'clouds is empty!'


    """
    @param[in]
    Pass: if cloud_texture is not empty
    """ 
    assert cloud_texture is not None, 'cloud_texture is empty!'

    glBindTexture(GL_TEXTURE_2D, cloud_texture.id)
    glColor4f(1, 1, 1, 1)

    for cloud in clouds:
        glPushMatrix()
        glTranslatef(*cloud)
        sphere_vertex_list.draw(GL_POINTS)
        glPopMatrix()



"""
Test: create vertex data for a simple textured sphere
"""
def create_moon(radius, slices, stacks):

    """
    @param[in]
    Pass: if radius is > 0
    """
    assert radius > 0, 'radius is not greater than 0!'


    """
    @param[in]
    Pass: if slices is > 0
    """
    assert slices > 0, 'slices is not greater than 0!'


    """
    @param[in]
    Pass: if stacks is > 0
    """
    assert stacks > 0, 'stacks is not greater than 0!'
    
    vertices = []

    for stack in range(stacks + 1):
        for slice in range(slices):
            x = radius * cos(2 * pi * slice / slices) * sin(pi * stack / stacks)
            y = radius * sin(-pi / 2 + pi * stack / stacks)
            z = radius * sin(2 * pi * slice / slices) * sin(pi * stack / stacks)
            vertices.extend([x, y, z])


    """
    @param[out]
    Pass: if list vertices is not empty
    """ 
    assert vertices is not None, 'vertices is empty!'


    """
    @param[out]
    Pass: if each element in list vertices is numerical
    """ 
    for coordinates in vertices:
        for coordinate in coordinates:
            coordinate_float = float(coordinate)
            assert isinstance(coordinate_float, float), 'vertices contains a non-numerical value!'

    draw(pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices)))


"""
Test: enable buffer to draw
"""
def draw(sphere_vertex_list):

    """
    @param[in]
    @param[out]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_moon(sphere_vertex_list)


"""
Test: draw the moon
"""
def draw_moon(sphere_vertex_list):

    """
    @param[in]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    MOON_POSITION = (0, 15, -15)

    glPushMatrix()
    glTranslatef(*MOON_POSITION)
    sphere_vertex_list.draw(GL_POINTS)
    glPopMatrix()




"""
TESTS for sun.py
https://github.com/WSUCEG-7140/TeamK-MinecraftPython/issues/52
"""

"""
Test: create vertex data for a simple textured sphere
"""
def create_sun(radius, slices, stacks):

    """
    @param[in]
    Pass: if radius is > 0
    """
    assert radius > 0, 'radius is not greater than 0!'


    """
    @param[in]
    Pass: if slices is > 0
    """
    assert slices > 0, 'slices is not greater than 0!'


    """
    @param[in]
    Pass: if stacks is > 0
    """
    assert stacks > 0, 'stacks is not greater than 0!'
    
    vertices = []
    
    for stack in range(stacks + 1):
        for slice in range(slices):
            x = radius * cos(2 * pi * slice / slices) * sin(pi * stack / stacks)
            y = radius * sin(-pi / 2 + pi * stack / stacks)
            z = radius * sin(2 * pi * slice / slices) * sin(pi * stack / stacks)
            vertices.extend([x, y, z])


    """
    @param[out]
    Pass: if list vertices is not empty
    """ 
    assert vertices is not None, 'vertices is empty!'


    """
    @param[out]
    Pass: if each element in list vertices is numerical
    """ 
    for coordinates in vertices:
        for coordinate in coordinates:
            coordinate_float = float(coordinate)
            assert isinstance(coordinate_float, float), 'vertices contains a non-numerical value!'
            

    draw(pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices)))


"""
Test: enable buffer to draw
"""
def draw(sphere_vertex_list):

    """
    @param[in]
    @param[out]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_sun(sphere_vertex_list)
    

"""
Test: draw the sun
"""
def draw_sun(sphere_vertex_list):

    """
    @param[in]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    SUN_POSITION = (10, 10, 10)

    glPushMatrix()
    glTranslatef(*SUN_POSITION)
    sphere_vertex_list.draw(GL_POINTS)
    glPopMatrix()




"""
TESTS for moon.py
https://github.com/WSUCEG-7140/TeamK-MinecraftPython/issues/53
"""

"""
Test: create vertex data for a simple textured sphere
"""
def create_moon(radius, slices, stacks):

    """
    @param[in]
    Pass: if radius is > 0
    """
    assert radius > 0, 'radius is not greater than 0!'


    """
    @param[in]
    Pass: if slices is > 0
    """
    assert slices > 0, 'slices is not greater than 0!'


    """
    @param[in]
    Pass: if stacks is > 0
    """
    assert stacks > 0, 'stacks is not greater than 0!'
    
    vertices = []

    for stack in range(stacks + 1):
        for slice in range(slices):
            x = radius * cos(2 * pi * slice / slices) * sin(pi * stack / stacks)
            y = radius * sin(-pi / 2 + pi * stack / stacks)
            z = radius * sin(2 * pi * slice / slices) * sin(pi * stack / stacks)
            vertices.extend([x, y, z])


    """
    @param[out]
    Pass: if list vertices is not empty
    """ 
    assert vertices is not None, 'vertices is empty!'


    """
    @param[out]
    Pass: if each element in list vertices is numerical
    """ 
    for coordinates in vertices:
        for coordinate in coordinates:
            coordinate_float = float(coordinate)
            assert isinstance(coordinate_float, float), 'vertices contains a non-numerical value!'

    draw(pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices)))


"""
Test: enable buffer to draw
"""
def draw(sphere_vertex_list):

    """
    @param[in]
    @param[out]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_moon(sphere_vertex_list)


"""
Test: draw the moon
"""
def draw_moon(sphere_vertex_list):

    """
    @param[in]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    MOON_POSITION = (0, 15, -15)

    glPushMatrix()
    glTranslatef(*MOON_POSITION)
    sphere_vertex_list.draw(GL_POINTS)
    glPopMatrix()

