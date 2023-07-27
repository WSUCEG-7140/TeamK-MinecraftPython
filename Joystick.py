import pyglet.input  # Import the pyglet input module for joystick support
import threading  # Import the threading module for multi-threading
import math  # Import the math module for mathematical operations
import time  # Import the time module for time-related operations

class Joystick():
    def __init__(self, game):
        """
        Constructor for the Joystick class.

        @param[in] game (Game): An instance of the Game class representing the game environment.
        """
        self.game = game
        self.init_joysticks(pyglet.input.get_joysticks())

        self.camera_sensitivity = 0.007  # Set the camera sensitivity for joystick movement
        self.joystick_deadzone = 0.25  # Set the deadzone for joystick input
        self.update_delay = 0.15  # Set the delay for updating joystick input
        self.last_update = 0  # Initialize the last update time

        self.joystick_move = [0, 0]  # Initialize the joystick movement values (x, y)
        self.joystick_look = [0, 0]  # Initialize the joystick look values (rx, ry)
        self.joystick_interact = [0, 0]  # Initialize the joystick interact values (z)

        self.joystick_updater = threading.Thread(target=self.updater, daemon=True, name="Joystick Updater")  # Create a thread for updating joystick input
        self.joystick_updater.start()  # Start the joystick updater thread

    def updater(self):
        """
        Thread function that continuously checks for changes in connected joysticks and reinitializes them if needed.
        """
        while True:
            if len(pyglet.input.get_joysticks()) != len(self.joysticks):  # Check if the number of connected joysticks has changed
                self.init_joysticks(pyglet.input.get_joysticks())  # Reinitialize the joysticks
            
            time.sleep(2)  # Sleep for 2 seconds before checking again

    def init_joysticks(self, joysticks):
        """
        Initialize the joysticks and assign event handlers for button presses, releases, axis motions, and hat motions.

        @param[in] joysticks (list): A list of pyglet.input.Joystick objects representing the connected joysticks.
        """
        self.joysticks = joysticks  # Set the joysticks to the given list of joysticks

        for joystick in self.joysticks:
            joystick.on_joybutton_press = self.on_joybutton_press  # Assign the on_joybutton_press event handler
            joystick.on_joybutton_release = self.on_joybutton_release  # Assign the on_joybutton_release event handler
            joystick.on_joyaxis_motion = self.on_joyaxis_motion  # Assign the on_joyaxis_motion event handler
            joystick.on_joyhat_motion = self.on_joyhat_motion  # Assign the on_joyhat_motion event handler
            joystick.open(exclusive=True)  # Open the joystick in exclusive mode

    def update_controller(self):
        """
        Update the controller based on the joystick input, adjusting player rotation and movement speed.
        """
        if not self.game.mouse_captured or not self.joysticks:  # Check if the mouse is not captured or no joysticks are connected
            return  # Return without updating the controller

        self.game.player.rotation[0] += self.joystick_look[0] * self.camera_sensitivity  # Update the player's horizontal rotation based on joystick look input
        self.game.player.rotation[1] += -self.joystick_look[1] * self.camera_sensitivity  # Update the player's vertical rotation based on joystick look input

        self.game.player.rotation[1] = max(-math.tau / 4, min(math.tau / 4, self.game.player.rotation[1]))  # Clamp the vertical rotation within a certain range

        if round(max(self.joystick_interact)) > 0 and (self.last_update + self.update_delay) <= time.process_time():  # Check if the interact joystick input is active and enough time has passed since the last update
            if round(self.joystick_interact[0]) > 0:
                self.interact(self.InteractMode.BREAK)  # Call the interact method with the corresponding interaction mode
            if round(self.joystick_interact[1]) > 0:
                self.interact(self.InteractMode.PLACE)  # Call the interact method with the corresponding interaction mode

            self.last_update = time.process_time()  # Update the last update time

    def on_joybutton_press(self, joystick, button):
        """
        Event handler for joystick button press events.

        @param[in] joystick (pyglet.input.Joystick): The joystick that triggered the event.
        @param[in] button (int): The index of the button that was pressed.
        """
        if "xbox" in joystick.device.name.lower():  # Check if the joystick is an Xbox controller
            if button == 1:
                self.misc(self.MiscMode.RANDOM)  # Call the misc method with the corresponding misc mode
            elif button == 2:
                self.interact(self.InteractMode.PICK)  # Call the interact method with the corresponding interaction mode
            elif button == 3:
                self.misc(self.MiscMode.SAVE)  # Call the misc method with the corresponding misc mode

            elif button == 0:
                self.start_move(self.MoveMode.UP)  # Call the start_move method with the corresponding move mode
            elif button == 9:
                self.start_move(self.MoveMode.DOWN)  # Call the start_move method with the corresponding move mode

            elif button == 8:
                if self.game.player.target_speed == player.SPRINTING_SPEED:
                    self.end_modifier(self.ModifierMode.SPRINT)  # Call the end_modifier method with the corresponding modifier mode
                elif self.game.player.target_speed == player.WALKING_SPEED:
                    self.start_modifier(self.ModifierMode.SPRINT)  # Call the start_modifier method with the corresponding modifier mode

        elif "wireless controller" == joystick.device.name.lower():  # Check if the joystick is a wireless controller
            if button == 2:
                self.misc(self.MiscMode.RANDOM)  # Call the misc method with the corresponding misc mode
            elif button == 0:
                self.interact(self.InteractMode.PICK)  # Call the interact method with the corresponding interaction mode
            elif button == 3:
                self.misc(self.MiscMode.SAVE)  # Call the misc method with the corresponding misc mode

            elif button == 1:
                self.start_move(self.MoveMode.UP)  # Call the start_move method with the corresponding move mode
            elif button == 11:
                self.start_move(self.MoveMode.DOWN)  # Call the start_move method with the corresponding move mode

            elif button == 10:
                if self.game.player.target_speed == player.SPRINTING_SPEED:
                    self.end_modifier(self.ModifierMode.SPRINT)  # Call the end_modifier method with the corresponding modifier mode
                elif self.game.player.target_speed == player.WALKING_SPEED:
                    self.start_modifier(self.ModifierMode.SPRINT)  # Call the start_modifier method with the corresponding modifier mode

    def on_joybutton_release(self, joystick, button):
        """
        Event handler for joystick button release events.

        @param[in] joystick (pyglet.input.Joystick): The joystick that triggered the event.
        @param[in] button (int): The index of the button that was released.
        """
        if "xbox" in joystick.device.name.lower():  # Check if the joystick is an Xbox controller
            if button == 0:
                self.end_move(self.MoveMode.UP)  # Call the end_move method with the corresponding move mode
            elif button == 9:
                self.end_move(self.MoveMode.DOWN)  # Call the end_move method with the corresponding move mode

        elif "wireless controller" == joystick.device.name.lower():  # Check if the joystick is a wireless controller
            if button == 1:
                self.end_move(self.MoveMode.UP)  # Call the end_move method with the corresponding move mode
            elif button == 11:
                self.end_move(self.MoveMode.DOWN)  # Call the end_move method with the corresponding move mode

    def on_joyaxis_motion(self, joystick, axis, value):
        """
        Event handler for joystick axis motion events.

        @param[in] joystick (pyglet.input.Joystick): The joystick that triggered the event.
        @param[in] axis (str): The name of the axis that changed its value (e.g., "x", "y", "z", "rx", "ry", "rz").
        @param[in] value (float): The current value of the axis motion.
        """
        if abs(value) < self.joystick_deadzone:  # Check if the joystick value is within the deadzone
            value = 0  # Set the joystick value to zero

        if "xbox" in joystick.device.name.lower():  # Check if the joystick is an Xbox controller
            if axis == "x":
                if math.ceil(value) > 0 and self.joystick_move[0] == 0:
                    self.start_move(self.MoveMode.RIGHT)  # Call the start_move method with the corresponding move mode
                elif math.floor(value) < 0 and self.joystick_move[0] == 0:
                    self.start_move(self.MoveMode.LEFT)  # Call the start_move method with the corresponding move mode
                elif value == 0 and math.ceil(self.joystick_move[0]) > 0:
                    self.end_move(self.MoveMode.RIGHT)  # Call the end_move method with the corresponding move mode
                elif value == 0 and math.floor(self.joystick_move[0]) < 0:
                    self.end_move(self.MoveMode.LEFT)  # Call the end_move method with the corresponding move mode

                self.joystick_move[0] = value  # Update the joystick move value for x-axis
            elif axis == "y":
                if math.ceil(value) > 0 and self.joystick_move[1] == 0:
                    self.start_move(self.MoveMode.BACKWARD)  # Call the start_move method with the corresponding move mode
                elif math.floor(value) < 0 and self.joystick_move[1] == 0:
                    self.start_move(self.MoveMode.FORWARD)  # Call the start_move method with the corresponding move mode
                elif value == 0 and math.ceil(self.joystick_move[1]) > 0:
                    self.end_move(self.MoveMode.BACKWARD)  # Call the end_move method with the corresponding move mode
                elif value == 0 and math.floor(self.joystick_move[1]) < 0:
                    self.end_move(self.MoveMode.FORWARD)  # Call the end_move method with the corresponding move mode

                self.joystick_move[1] = value  # Update the joystick move value for y-axis

            if axis == "rx":
                self.joystick_look[0] = value  # Update the joystick look value for rx-axis
            if axis == "ry":
                self.joystick_look[1] = value  # Update the joystick look value for ry-axis

            if axis == "z":
                if value < 0:
                    self.joystick_interact[0] = -value  # Update the joystick interact value for negative z-axis value
                if value > 0:
                    self.joystick_interact[1] = value  # Update the joystick interact value for positive z-axis value

        elif "wireless controller" == joystick.device.name.lower():  # Check if the joystick is a wireless controller
            if axis == "x":
                if math.ceil(value) > 0 and self.joystick_move[0] == 0:
                    self.start_move(self.MoveMode.RIGHT)  # Call the start_move method with the corresponding move mode
                elif math.floor(value) < 0 and self.joystick_move[0] == 0:
                    self.start_move(self.MoveMode.LEFT)  # Call the start_move method with the corresponding move mode
                elif value == 0 and math.ceil(self.joystick_move[0]) > 0:
                    self.end_move(self.MoveMode.RIGHT)  # Call the end_move method with the corresponding move mode
                elif value == 0 and math.floor(self.joystick_move[0]) < 0:
                    self.end_move(self.MoveMode.LEFT)  # Call the end_move method with the corresponding move mode

                self.joystick_move[0] = value  # Update the joystick move value for x-axis
            elif axis == "y":
                if math.ceil(value) > 0 and self.joystick_move[1] == 0:
                    self.start_move(self.MoveMode.BACKWARD)  # Call the start_move method with the corresponding move mode
                elif math.floor(value) < 0 and self.joystick_move[1] == 0:
                    self.start_move(self.MoveMode.FORWARD)  # Call the start_move method with the corresponding move mode
                elif value == 0 and math.ceil(self.joystick_move[1]) > 0:
                    self.end_move(self.MoveMode.BACKWARD)  # Call the end_move method with the corresponding move mode
                elif value == 0 and math.floor(self.joystick_move[1]) < 0:
                    self.end_move(self.MoveMode.FORWARD)  # Call the end_move method with the corresponding move mode

                self.joystick_move[1] = value  # Update the joystick move value for y-axis

            if axis == "z":
                self.joystick_look[0] = value  # Update the joystick look value for z-axis
            if axis == "rz":
                self.joystick_look[1] = value  # Update the joystick look value for rz-axis

            print(axis)  # Print the axis value

    def on_joyhat_motion(self, joystick, hat_x, hat_y):
        """
        Event handler for joystick hat motion events.

        @param[in] joystick (pyglet.input.Joystick): The joystick that triggered the event.
        @param[in] hat_x (int): The x-coordinate of the hat motion (-1, 0, or 1).
        @param[in] hat_y (int): The y-coordinate of the hat motion (-1, 0, or 1).
        """
        pass  # Do nothing for joystick hat motion
