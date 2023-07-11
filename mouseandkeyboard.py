import pyglet.window

import controller
import math

class Keyboard_Mouse(controller.Controller):
	def __init__(self, game):
		super().__init__(game)

		self.game.on_mouse_press = self.on_mouse_press
		self.game.on_mouse_motion = self.on_mouse_motion
		self.game.on_mouse_drag = self.on_mouse_drag

		self.game.on_key_press = self.on_key_press
		self.game.on_key_release = self.on_key_release

	def on_mouse_press(self, x, y, button, modifiers):
		if not self.game.mouse_captured:
			self.game.mouse_captured = True
			self.game.set_exclusive_mouse(True)

			return

		if button == pyglet.window.mouse.RIGHT: self.interact(self.InteractMode.PLACE)
		elif button == pyglet.window.mouse.LEFT: self.interact(self.InteractMode.BREAK)
		elif button == pyglet.window.mouse.MIDDLE: self.interact(self.InteractMode.PICK)

	def on_mouse_motion(self, x, y, delta_x, delta_y):
		if self.game.mouse_captured:
			sensitivity = 0.004

			self.game.player.rotation[0] += delta_x * sensitivity
			self.game.player.rotation[1] += delta_y * sensitivity

			self.game.player.rotation[1] = max(-math.tau / 4, min(math.tau / 4, self.game.player.rotation[1]))

	def on_mouse_drag(self, x, y, delta_x, delta_y, buttons, modifiers):
		self.on_mouse_motion(x, y, delta_x, delta_y)

	def on_key_press(self, key, modifiers):
		if not self.game.mouse_captured:
			return

		if key == pyglet.window.key.D: self.start_move(self.MoveMode.RIGHT)
		elif key == pyglet.window.key.A: self.start_move(self.MoveMode.LEFT)
		elif key == pyglet.window.key.W: self.start_move(self.MoveMode.FORWARD)
		elif key == pyglet.window.key.S: self.start_move(self.MoveMode.BACKWARD)
		elif key == pyglet.window.key.SPACE : self.start_move(self.MoveMode.UP)
		elif key == pyglet.window.key.LSHIFT: self.start_move(self.MoveMode.DOWN)

		elif key == pyglet.window.key.LCTRL : self.start_modifier(self.ModifierMode.SPRINT)

		elif key == pyglet.window.key.E: self.misc(self.MiscMode.SPAWN)
		elif key == pyglet.window.key.F: self.misc(self.MiscMode.FLY)
		elif key == pyglet.window.key.G: self.misc(self.MiscMode.RANDOM)
		elif key == pyglet.window.key.O: self.misc(self.MiscMode.SAVE)
		elif key == pyglet.window.key.R: self.misc(self.MiscMode.TELEPORT)
		elif key == pyglet.window.key.ESCAPE: self.misc(self.MiscMode.ESCAPE)
		elif key == pyglet.window.key.F6: self.misc(self.MiscMode.SPEED_TIME)
		elif key == pyglet.window.key.F11: self.misc(self.MiscMode.FULLSCREEN)
		elif key == pyglet.window.key.F3: self.misc(self.MiscMode.TOGGLE_F3)
		elif key == pyglet.window.key.F10: self.misc(self.MiscMode.TOGGLE_AO)

	def on_key_release(self, key, modifiers):
		if not self.game.mouse_captured:
			return

		if key == pyglet.window.key.D: self.end_move(self.MoveMode.RIGHT)
		elif key == pyglet.window.key.A: self.end_move(self.MoveMode.LEFT)
		elif key == pyglet.window.key.W: self.end_move(self.MoveMode.FORWARD)
		elif key == pyglet.window.key.S: self.end_move(self.MoveMode.BACKWARD)
		elif key == pyglet.window.key.SPACE : self.end_move(self.MoveMode.UP)
		elif key == pyglet.window.key.LSHIFT: self.end_move(self.MoveMode.DOWN)

		elif key == pyglet.window.key.LCTRL : self.end_modifier(self.ModifierMode.SPRINT)


#test cases

import unittest
import pyglet.window
import math

import controller

class TestKeyboardMouseEventHandling(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test dependencies or initialize game-related objects
        self.game = YourGameClass()  # Replace with your actual game class
        self.controller = controller.Keyboard_Mouse(self.game)  # Create an instance of the controller
        self.controller.InteractMode = controller.InteractMode  # Import InteractMode enum
        self.controller.MoveMode = controller.MoveMode  # Import MoveMode enum
        self.controller.ModifierMode = controller.ModifierMode  # Import ModifierMode enum
        self.controller.MiscMode = controller.MiscMode  # Import MiscMode enum
        self.interact_called_with = None
        self.on_mouse_motion_called_with = None
        self.start_move_called_with = None
        self.start_modifier_called_with = None
        self.misc_called_with = None
        self.end_move_called_with = None

    def tearDown(self):
        # Clean up after each test if needed
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        # Simulate the on_mouse_press event
        self.controller.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        # Simulate the on_mouse_motion event
        self.controller.on_mouse_motion(x, y, delta_x, delta_y)

    def on_mouse_drag(self, x, y, delta_x, delta_y, buttons, modifiers):
        # Simulate the on_mouse_drag event
        self.controller.on_mouse_drag(x, y, delta_x, delta_y, buttons, modifiers)

    def on_key_press(self, key, modifiers):
        # Simulate the on_key_press event
        self.controller.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        # Simulate the on_key_release event
        self.controller.on_key_release(key, modifiers)

    def test_mouse_right_click(self):
        # Simulate a mouse right-click event
        self.on_mouse_press(100, 200, pyglet.window.mouse.RIGHT, pyglet.window.key.MOD_SHIFT)
        # Verify that the "interact" method is called with InteractMode.PLACE
        self.assertEqual(self.controller.interact_called_with, self.controller.InteractMode.PLACE)

    def test_mouse_left_click(self):
        # Simulate a mouse left-click event
        self.on_mouse_press(200, 300, pyglet.window.mouse.LEFT, pyglet.window.key.MOD_CTRL)
        # Verify that the "interact" method is called with InteractMode.BREAK
        self.assertEqual(self.controller.interact_called_with, self.controller.InteractMode.BREAK)

    def test_mouse_middle_click(self):
        # Simulate a mouse middle-click event
        self.on_mouse_press(300, 400, pyglet.window.mouse.MIDDLE, pyglet.window.key.MOD_ALT)
        # Verify that the "interact" method is called with InteractMode.PICK
        self.assertEqual(self.controller.interact_called_with, self.controller.InteractMode.PICK)

    def test_mouse_motion(self):
        # Simulate mouse motion with specified delta_x and delta_y values
        self.on_mouse_motion(0, 0, 10, 20)
        # Verify that the player's rotation is updated correctly
        expected_rotation = [10 * 0.004, 20 * 0.004]
        self.assertEqual(self.game.player.rotation, expected_rotation)

    def test_mouse_drag(self):
        # Simulate mouse drag events with specified parameters
        self.on_mouse_drag(100, 100, 5, 5, pyglet.window.mouse.LEFT, pyglet.window.key.MOD_NONE)
        # Ensure that the "on_mouse_motion" method is called correctly
        expected_on_mouse_motion_args = (100, 100, 5, 5)
        self.assertEqual(self.on_mouse_motion_called_with, expected_on_mouse_motion_args)

    def test_key_press_movement(self):
        # Simulate key press for movement (e.g., W, A, S, D)
        self.on_key_press(pyglet.window.key.W, pyglet.window.key.MOD_NONE)
        # Verify that the "start_move" method is called with the correct MoveMode
        self.assertEqual(self.controller.start_move_called_with, self.controller.MoveMode.FORWARD)

    def test_key_press_modifier(self):
        # Simulate key press for modifier (e.g., LCTRL)
        self.on_key_press(pyglet.window.key.LCTRL, pyglet.window.key.MOD_NONE)
        # Ensure that the "start_modifier" method is called with the correct ModifierMode
        self.assertEqual(self.controller.start_modifier_called_with, self.controller.ModifierMode.SPRINT)

    def test_key_press_miscellaneous(self):
        # Simulate key press for miscellaneous actions (e.g., E, F, G, O, R, ESCAPE)
        self.on_key_press(pyglet.window.key.G, pyglet.window.key.MOD_SHIFT)
        # Verify that the corresponding methods are invoked with the expected MiscMode
        self.assertEqual(self.controller.misc_called_with, self.controller.MiscMode.RANDOM)

    def test_key_press_toggle(self):
        # Simulate key press for toggle actions (e.g., F3, F10, F11)
        self.on_key_press(pyglet.window.key.F11, pyglet.window.key.MOD_NONE)
        # Ensure that the appropriate methods are called with the correct MiscMode
        self.assertEqual(self.controller.misc_called_with, self.controller.MiscMode.FULLSCREEN)

    def test_key_release(self):
        # Simulate key release
        self.on_key_release(pyglet.window.key.D, pyglet.window.key.MOD_NONE)
        # Verify that the "end_move" method is called correctly
        self.assertEqual(self.controller.end_move_called_with, self.controller.MoveMode.RIGHT)

if __name__ == '__main__':
    unittest.main()

