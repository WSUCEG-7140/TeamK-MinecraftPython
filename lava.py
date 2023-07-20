class Block:
    def __init__(self):
        self.is_melted = False  # Indicates whether the block is melted or not

    def on_collision(self, other):
        """
        Placeholder method for handling collisions.

        Parameters:
            other (Block): The other block involved in the collision.
        """
        pass


class SnowBlock(Block):
    def on_collision(self, other):
        """
        Handle collisions with other blocks.

        If the SnowBlock collides with Lava, it will be melted.

        Parameters:
            other (Block): The other block involved in the collision.
        """
        if isinstance(other, Lava):
            self.is_melted = True  # Snow block is melted if it collides with lava


class Lava(Block):
    pass


# Usage example:
snow_block = SnowBlock()
lava = Lava()

# Simulating collision
snow_block.on_collision(lava)

if snow_block.is_melted:
    print("Snow block melted!")
else:
    print("Snow block not melted!")
