
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
