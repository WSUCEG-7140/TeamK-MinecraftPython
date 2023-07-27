import pyglet.window
import math

class Keyboard_Mouse():
    """
    A class that handles keyboard and mouse events for the game.

    @pre The 'game' parameter in the constructor must be a valid game object.
    @post The appropriate event handlers will be set for the game object to respond to keyboard and mouse events.
    """

    def __init__(self, game):
        """
        Initializes the Keyboard_Mouse object.

        @param game: The game object.
        """
        # Check preconditions
        assert isinstance(game, Game), "Invalid 'game' parameter. Expected a valid Game object."

        self.game = game  # Initialize the 'game' instance variable

        self.mouse_captured = False  # Initialize the 'mouse_captured' instance variable to False

        # Set the game's mouse and keyboard event handlers
        self.game.on_mouse_press = self.on_mouse_press
        self.game.on_mouse_motion = self.on_mouse_motion
        self.game.on_mouse_drag = self.on_mouse_drag
        self.game.on_key_press = self.on_key_press
        self.game.on_key_release = self.on_key_release

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Handles mouse press events.

        @param[in] x: The x-coordinate of the mouse position.
        @param[in] y: The y-coordinate of the mouse position.
        @param[in] button: The button that was pressed.
        @param[in] modifiers: The key modifiers that were active.
        """
        # No preconditions for mouse press events

        if not self.mouse_captured:
            self.mouse_captured = True
            self.game.set_exclusive_mouse(True)
            return

        if button == pyglet.window.mouse.RIGHT:
            self.interact(self.InteractMode.PLACE)
        elif button == pyglet.window.mouse.LEFT:
            self.interact(self.InteractMode.BREAK)
        elif button == pyglet.window.mouse.MIDDLE:
            self.interact(self.InteractMode.PICK)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Handles mouse motion events.

        @param[in] x: The x-coordinate of the mouse position.
        @param[in] y: The y-coordinate of the mouse position.
        @param[in] delta_x: The change in the x-coordinate since the last motion event.
        @param[in] delta_y: The change in the y-coordinate since the last motion event.
        """
        # No preconditions for mouse motion events

        if self.mouse_captured:
            sensitivity = 0.004

            self.game.player.rotation[0] += delta_x * sensitivity
            self.game.player.rotation[1] += delta_y * sensitivity

            self.game.player.rotation[1] = max(-math.tau / 4, min(math.tau / 4, self.game.player.rotation[1]))

    def on_mouse_drag(self, x, y, delta_x, delta_y, buttons, modifiers):
        """
        Handles mouse drag events.

        @param[in] x: The x-coordinate of the mouse position.
        @param[in] y: The y-coordinate of the mouse position.
        @param[in] delta_x: The change in the x-coordinate since the last drag event.
        @param[in] delta_y: The change in the y-coordinate since the last drag event.
        @param[in] buttons: The mouse buttons that are currently pressed.
        @param[in] modifiers: The key modifiers that are active.
        """
        # No preconditions for mouse drag events

        self.on_mouse_motion(x, y, delta_x, delta_y)

    def on_key_press(self, key, modifiers):
        """
        Handles key press events.

        @param[in] key: The key that was pressed.
        @param[in] modifiers: The key modifiers that were active.
        """
        # Check preconditions
        assert self.mouse_captured, "Key press events should not be handled when the mouse is not captured."

        if key == pyglet.window.key.D:
            self.start_move(self.MoveMode.RIGHT)
        elif key == pyglet.window.key.A:
            self.start_move(self.MoveMode.LEFT)
        elif key == pyglet.window.key.W:
            self.start_move(self.MoveMode.FORWARD)
        elif key == pyglet.window.key.S:
            self.start_move(self.MoveMode.BACKWARD)
        elif key == pyglet.window.key.SPACE:
            self.start_move(self.MoveMode.UP)
        elif key == pyglet.window.key.LSHIFT:
            self.start_move(self.MoveMode.DOWN)

    def on_key_release(self, key, modifiers):
        """
        Handles key release events.

        @param[in] key: The key that was released.
        @param[in] modifiers: The key modifiers that were active.
        """
        # Check preconditions
        assert self.mouse_captured, "Key release events should not be handled when the mouse is not captured."

        if key == pyglet.window.key.D:
            self.end_move(self.MoveMode.RIGHT)
        elif key == pyglet.window.key.A:
            self.end_move(self.MoveMode.LEFT)
        elif key == pyglet.window.key.W:
            self.end_move(self.MoveMode.FORWARD)
        elif key == pyglet.window.key.S:
            self.end_move(self.MoveMode.BACKWARD)
        elif key == pyglet.window.key.SPACE:
            self.end_move(self.MoveMode.UP)
        elif key == pyglet.window.key.LSHIFT:
            self.end_move(self.MoveMode.DOWN)
        elif key == pyglet.window.key.LCTRL:
            self.end_modifier(self.ModifierMode.SPRINT)
