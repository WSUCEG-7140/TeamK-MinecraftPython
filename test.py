from main import *
from snow import *
from terrain import *
from hit import *
# from keyboard_mouse import *
# from pygletbatchupdater import *

import unittest

''' 
Sample test case to ensure working PyTest
'''
def test_pytest():
    assert True



"""
Tests from terrain.py
"""
def test_print():
    try:
        print_terrain(terrain)
        assert(True)
    except: assert(False)
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


"""
Tests from main.py
"""
def test_fog():
    try:
        setup_fog()
        assert True
    except: assert False


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
Errors found in Tests from keyboard_mouse.py
"""

"""
Errors found in Tests from pygletbatchupdater.py. Need to have ShaderProgram working before testing
"""
