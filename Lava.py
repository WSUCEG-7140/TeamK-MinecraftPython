class Block:
    def __init__(self):
        """
        Initializes a generic block.

        @note Contracts:
        - Postconditions:
            - The 'is_melted' attribute is set to False by default.
        """
        self.is_melted = False  # Indicates whether the block is melted or not

    def on_collision(self, other):
        """
        Placeholder method for handling collisions.

        @param other (Block): The other block involved in the collision.
        """
        # No preconditions or postconditions for this placeholder method.
        pass


class SnowBlock(Block):
    def on_collision(self, other):
        """
        Handle collisions with other blocks.

        If the SnowBlock collides with Lava, it will be melted.

        @param other (Block): The other block involved in the collision.
        """
        # Check precondition
        assert isinstance(other, Block), "Invalid 'other' parameter. Expected a Block instance."

        if isinstance(other, Lava):
            self.is_melted = True  # Snow block is melted if it collides with lava

        # No postconditions needed

class Lava(Block):
    """
    A class representing a Lava block.

    @note Contracts:
    - Preconditions:
        None
    - Postconditions:
        None
    """
    pass


# Usage example:
snow_block = SnowBlock()
lava = Lava()

# Simulating collision
snow_block.on_collision(lava)

# Check the result
if snow_block.is_melted:
    print("Snow block melted!")
else:
    print("Snow block not melted!")
