# Define the dimensions of the terrain
terrain_width = 10
terrain_height = 5
terrain_depth = 10

# Create an empty terrain
terrain = [[[None for _ in range(terrain_depth)] for _ in range(terrain_height)] for _ in range(terrain_width)]

# Function to add water blocks to the terrain
def add_water(start_x, start_y, start_z, width, height, depth):
    """
    Add water blocks to the terrain within the specified coordinates and dimensions.

    Args:
        start_x (int): The starting x-coordinate.
        start_y (int): The starting y-coordinate.
        start_z (int): The starting z-coordinate.
        width (int): The width of the water area.
        height (int): The height of the water area.
        depth (int): The depth of the water area.

    """
    for x in range(start_x, start_x + width):
        for y in range(start_y, start_y + height):
            for z in range(start_z, start_z + depth):
                terrain[x][y][z] = "blue"

# Example usage: Adding water blocks to the terrain
add_water(3, 1, 3, 4, 1, 4)

# Printing the terrain
for y in range(terrain_height):
    for z in range(terrain_depth):
        for x in range(terrain_width):
            block = terrain[x][y][z]
            if block is None:
                print("  ", end="")
            else:
                print(block + " ", end="")
        print()
    print()
