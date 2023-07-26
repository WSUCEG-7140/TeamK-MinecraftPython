#test cases for josephreddy-#issue16

"""
Tests from Keyboard_mouse.py
"""

import unittest

class Keyboard:
    """A class representing a keyboard for movement."""

    def __init__(self):
        """Initialize the Keyboard object."""
        self.x = 0
        self.y = 0

    def move_left(self):
        """Move the keyboard position to the left."""
        self.x -= 1

    def move_right(self):
        """Move the keyboard position to the right."""
        self.x += 1

    def move_up(self):
        """Move the keyboard position upwards."""
        self.y += 1

    def move_down(self):
        """Move the keyboard position downwards."""
        self.y -= 1

class Mouse:
    """A class representing a mouse for movement."""

    def __init__(self):
        """Initialize the Mouse object."""
        self.x = 0
        self.y = 0

    def move(self, delta_x, delta_y):
        """
        Move the mouse position by the given delta values.

        Args:
            delta_x (int): The change in the x-coordinate.
            delta_y (int): The change in the y-coordinate.
        """
        self.x += delta_x
        self.y += delta_y

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
