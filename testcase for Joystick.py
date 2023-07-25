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
