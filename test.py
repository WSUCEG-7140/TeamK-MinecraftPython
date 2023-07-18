from main import *
from snow import *
from terrain import *
# from pygletbatchupdater import *
# from hit import *
# from keyboard_mouse import *


import unittest

''' Sample test case to ensure working PyTest'''
def test_pytest():
    assert True



"""
Tests from terrain.py
"""

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


"""
Tests from main.py
"""
def test_fog():
    try:
        setup_fog()
        assert True
    except:
        assert False

"""
Errors found in Tests from pygletbatchupdater.py
"""



"""
Errors found in Tests from hit.py
"""




"""
Errors found in Tests from keyboard_mouse.py
"""




"""
Tests from snow.py
"""
class SnowBlockTestCase(unittest.TestCase):
    def test_add_snow_block_to_inventory(self):
        player = Player()
        snow_block = SnowBlock()
        player.add_item_to_inventory(snow_block)
        self.assertIn(snow_block, player.inventory)  # Check if the snow block is added to the player's inventory

    def test_render_snow_block_in_inventory(self):
        player = Player()
        inventory = Inventory()
        snow_block = SnowBlock()
        inventory.add_item("White Block (Snow)")
        inventory_renderer = InventoryRenderer()
        rendered_inventory = inventory_renderer.render(inventory)
        self.assertIsNotNone(rendered_inventory)  # Check if the rendered inventory is not None
        self.assertIn("White Block (Snow)", rendered_inventory)  # Check if the snow block is rendered in the inventory

    def test_slipperiness_of_snow_block(self):
        snow_block = SnowBlock()
        self.assertAlmostEqual(snow_block.slipperiness, 0.6, delta=0.001)  # Check if the slipperiness value is approximately 0.6

    def test_snow_block_not_broken_without_shovel(self):
        player = Player()
        snow_block = SnowBlock()
        snow_block.on_player_interact(player)
        self.assertFalse(snow_block.is_broken)  # Check if the snow block is not broken without a shovel

    def test_equip_tool(self):
        player = Player()
        shovel = Shovel()
        player.equip_tool(shovel)
        self.assertEqual(player.equipped_tool, shovel)  # Check if the player's equipped tool is the shovel


if __name__ == '__main__':
    unittest.main()