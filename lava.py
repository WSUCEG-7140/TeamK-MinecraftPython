class Block:
    def __init__(self):
        self.is_melted = False

    def on_collision(self, other):
        pass  # Placeholder method for handling collisions


class SnowBlock(Block):
    def on_collision(self, other):
        if isinstance(other, Lava):
            self.is_melted = True


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
