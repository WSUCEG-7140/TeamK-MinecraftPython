"""
Tests from terrain.py
"""
class Terrain:
    def __init__(self, width, height, depth):
        """
        @brief Class constructor to initialize the terrain.

        @param width (int): The width of the terrain.
        @param height (int): The height of the terrain.
        @param depth (int): The depth of the terrain.
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.terrain = [[[None for _ in range(depth)] for _ in range(height)] for _ in range(width)]

    def add_water(self, start_x, start_y, start_z, width, height, depth):
        """
        @brief Add water blocks to the terrain within the specified coordinates and dimensions.

        @param start_x (int): The starting x-coordinate.
        @param start_y (int): The starting y-coordinate.
        @param start_z (int): The starting z-coordinate.
        @param width (int): The width of the water area.
        @param height (int): The height of the water area.
        @param depth (int): The depth of the water area.
        """
        for x in range(start_x, start_x + width):
            for y in range(start_y, start_y + height):
                for z in range(start_z, start_z + depth):
                    self.terrain[x][y][z] = "blue"

    def print_terrain(self):
        """
        @brief Print the current state of the terrain.
        """
        for y in range(self.height):
            for z in range(self.depth):
                for x in range(self.width):
                    block = self.terrain[x][y][z]
                    if block is None:
                        print("  ", end="")
                    else:
                        print(block + " ", end="")
                print()
            print()


def test_terrain():
    # Test case 1
    terrain = Terrain(10, 5, 10)
    terrain.add_water(3, 1, 3, 4, 1, 4)
    print("Test Case 1:")
    terrain.print_terrain()
    print("\n")

    # Test case 2
    terrain = Terrain(10, 5, 10)
    terrain.add_water(0, 0, 0, 2, 3, 4)
    print("Test Case 2:")
    terrain.print_terrain()
    print("\n")

    # Test case 3
    terrain = Terrain(10, 5, 10)
    terrain.add_water(5, 0, 5, 3, 2, 3)
    print("Test Case 3:")
    terrain.print_terrain()
    print("\n")

    # Test case 4
    terrain = Terrain(10, 5, 10)
    terrain.add_water(0, 2, 0, 5, 1, 2)
    print("Test Case 4:")
    terrain.print_terrain()
    print("\n")

    # Test case 5
    terrain = Terrain(10, 5, 10)
    terrain.add_water(8, 4, 8, 2, 1, 2)
    print("Test Case 5:")
    terrain.print_terrain()
    print("\n")


    # Print the total number of tests run
    total_tests = 5  
    print(f"Total tests run: {total_tests}")

def main():
    test_terrain()

if __name__ == "__main__":
    main()

"""
 Expected Output:                                     
          blue blue blue        
          blue blue blue        
          blue blue blue  

ran 5 testcase in 0.01
ok
"""
