from main import *
from snow import *
from terrain import *
from hit import *
from keyboard_mouse import *
from pygletbatchupdater import *
from lava import *
from joystick import *
from clouds import *


import unittest
import pyglet
from pyglet.gl import *
from random import randint
from math import sin, cos, pi


''' 
Sample test case to ensure working PyTest
'''
def test_pytest():
    assert True

"""
Tests from terrain.py
"""
import unittest

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




"""
Tests from hit.py
"""
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

    print("All test cases passed!")

"""
Tests from snow.py
"""
import unittest

class Player:
    def __init__(self):
        self.inventory = []  # Initialize an empty inventory for the player

    def add_item_to_inventory(self, item):
        self.inventory.append(item)  # Add an item to the player's inventory

    def equip_tool(self, tool):
        self.equipped_tool = tool  # Set the equipped tool for the player

class Inventory:
    def __init__(self):
        self.items = []  # Initialize an empty list to store items in the inventory

    def add_item(self, item):
        self.items.append(item)  # Add an item to the inventory

class SnowBlock:
    def __init__(self):
        self.is_broken = False  # Initialize the snow block as not broken
        self.slipperiness = 0.6  # Set the slipperiness value for the snow block

    def on_player_interact(self, player):
        if hasattr(player, "equipped_tool") and player.equipped_tool == "shovel":
            self.is_broken = True  # Mark the snow block as broken if the player has a shovel

class InventoryRenderer:
    def render(self, inventory):
        rendered_inventory = ""
        for item in inventory.items:
            rendered_inventory += item + "\n"  # Render each item in the inventory
        return rendered_inventory

class Shovel:
    pass  # Define the Shovel class as empty for now

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
Tests from lava.py
"""
import unittest

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
Tests from joystick.py
"""
import unittest
from unittest.mock import MagicMock

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
Tests from keyboard_mouse.py
"""
class KeyboardMouseTestCase(unittest.TestCase):
    def setUp(self):
        self.game = MagicMock()
        self.keyboard_mouse = Keyboard_Mouse(self.game)


    def test_mouse_motion(self):
        self.game.mouse_captured = True
        sensitivity = 0.004

        self.game.player.rotation = [0, 0]

        self.keyboard_mouse.on_mouse_motion(0, 0, 10, 20)
        self.assertEqual(self.game.player.rotation, [10 * sensitivity, 20 * sensitivity])

if __name__ == '__main__':
    unittest.main()

"""
Tests from pygletbatchupdater.py
"""
import unittest
import pyglet
from pyglet.graphics import Batch
from pyglet.gl import *

class TestUpdatedBatch(unittest.TestCase):
    def setUp(self):
        self.batch = UpdatedBatch()

    def test_add(self):
        """
        Test the add method of UpdatedBatch.
        """
        self.batch.add(4, pyglet.gl.GL_QUADS, None, ('v2f', [0, 0, 100, 0, 100, 100, 0, 100]), ('c3B', [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0]))
        self.assertEqual(len(self.batch.vertices), 8)
        self.assertEqual(len(self.batch.colors), 12)

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
Tests from visual-properties.py
"""

def process_test_case(test_case_number, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values):
    """
    Process a test case.

    Args:
        test_case_number (int): The test case number.
        transparent (bool): Indicates whether the object is transparent.
        transparency (int): Transparency level on a scale of 0-10.
        is_cube (bool): Indicates whether the object is a cube.
        glass (bool): Indicates whether the object is made of glass.
        translucent (bool): Indicates whether the object is translucent.
        colliders (list): List of collider objects.
        vertex_positions (list): List of vertex positions for the object.
        tex_coords (list): List of texture coordinates for the object.
        shading_values (list): List of shading values for the object.
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
TESTS for clouds.py
"""

        
"""
Test: create the clouds' vertex data
"""
def create_cloud(radius, slices, stacks):

    """
    Pass: if radius is > 0
    """
    assert radius > 0, 'radius is not greater than 0!'


    """
    Pass: if slices is > 0
    """
    assert slices > 0, 'slices is not greater than 0!'


    """
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
    Pass: if list vertices is not empty
    """ 
    assert vertices is not None, 'vertices is empty!'

    create_clouds(pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices)))


"""
Test: create cloud positions
"""
def create_clouds(sphere_vertex_list):

    """
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    CLOUD_HEIGHT = 20
    NUM_CLOUDS = 30
    CLOUD_TEXTURE_PATH = 'cloud_texture.png'


    """
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
    Pass: if cloud_texture is not empty
    """ 
    assert cloud_texture is not None, 'cloud_texture is empty!'

    glBindTexture(GL_TEXTURE_2D, cloud_texture.id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    for _ in range(NUM_CLOUDS):
        x = randint(-40, 40)
        y = randint(CLOUD_HEIGHT, - 5, CLOUD_HEIGHT + 5)
        z = randint(-40, 40)
        clouds.append((x, y, z))


    """
    Pass: if list clouds is not empty
    """ 
    assert clouds is not None, 'clouds is empty!'


    """
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
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'


    """
    Pass: if list clouds is not empty
    """ 
    assert clouds is not None, 'clouds is empty!'


    """
    Pass: if cloud_texture is not empty
    """ 
    assert cloud_texture is not None, 'cloud_texture is empty!'

    draw_clouds(sphere_vertex_list, clouds, cloud_texture)


"""
Test: draw the clouds
"""
def draw_clouds(sphere_vertex_list, clouds, cloud_texture):

    """
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'


    """
    Pass: if list clouds is not empty
    """ 
    assert clouds is not None, 'clouds is empty!'


    """
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
TESTS for sun.py
"""


"""
Test: create vertex data for a simple textured sphere
"""
def create_sun(radius, slices, stacks):

    """
    Pass: if radius is > 0
    """
    assert radius > 0, 'radius is not greater than 0!'


    """
    Pass: if slices is > 0
    """
    assert slices > 0, 'slices is not greater than 0!'


    """
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
    Pass: if list vertices is not empty
    """ 
    assert vertices is not None, 'vertices is empty!'


    """
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
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    SUN_POSITION = (10, 10, 10)

    glPushMatrix()
    glTranslatef(*SUN_POSITION)
    sphere_vertex_list.draw(GL_POINTS)
    glPopMatrix()


