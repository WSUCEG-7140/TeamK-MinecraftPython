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
expected value:
Snow block melted!
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""
