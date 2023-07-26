"""
Tests from visual-properties.py
"""

def process_test_case(test_case_number, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values):
    """
    Process a test case.

    Args:
        test_case_number (int): The test case number.
        transparent (bool): Indicates whether the object is transparent.
        transparency (int): Transparency level on a scale of 0-10.
        is_cube (bool): Indicates whether the object is a cube.
        glass (bool): Indicates whether the object is made of glass.
        translucent (bool): Indicates whether the object is translucent.
        colliders (list): List of collider objects.
        vertex_positions (list): List of vertex positions for the object.
        tex_coords (list): List of texture coordinates for the object.
        shading_values (list): List of shading values for the object.
    """
    print(f"Test Case {test_case_number}:")
    print("Transparent:", transparent)
    print("Transparency:", transparency)
    print("Is Cube:", is_cube)
    print("Glass:", glass)
    print("Translucent:", translucent)
    print("Colliders:", colliders)
    print("Vertex Positions:", vertex_positions)
    print("Texture Coordinates:", tex_coords)
    print("Shading Values:", shading_values)
    print()

# Test Case 1
transparent = True
transparency = 2
is_cube = False
glass = False
translucent = False
colliders = []
vertex_positions = [
    [-0.3536, 0.5000,  0.3536, -0.3536, -0.5000,  0.3536,  0.3536, -0.5000, -0.3536,  0.3536, 0.5000, -0.3536],
    [-0.3536, 0.5000, -0.3536, -0.3536, -0.5000, -0.3536,  0.3536, -0.5000,  0.3536,  0.3536, 0.5000,  0.3536],
    [ 0.3536, 0.5000, -0.3536,  0.3536, -0.5000, -0.3536, -0.3536, -0.5000,  0.3536, -0.3536, 0.5000,  0.3536],
    [ 0.3536, 0.5000,  0.3536,  0.3536, -0.5000,  0.3536, -0.3536, -0.5000, -0.3536, -0.3536, 0.5000, -0.3536],
]
tex_coords = [
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]
shading_values = [
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
]

process_test_case(1, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values)

# Test Case 2
transparent = False
transparency = 0
is_cube = True
glass = False
translucent = False
colliders = []
vertex_positions = [
    [-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5],
    [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5],
    [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5],
    [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5],
]
tex_coords = [
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
]
shading_values = [
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
]

process_test_case(2, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values)

# Test Case 3
transparent = True
transparency = 1
is_cube = True
glass = True
translucent = False
colliders = [[-0.5, -0.5, -0.5, 0.5, 0.5, 0.5]]
vertex_positions = [
    [-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5],
    [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5],
    [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5],
    [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5],
]
tex_coords = [
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
]
shading_values = [
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
]

process_test_case(3, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values)

# Test Case 4
transparent = False
transparency = 0
is_cube = True
glass = False
translucent = True
colliders = []
vertex_positions = [
    [-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5],
    [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5],
    [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5],
    [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5],
]
tex_coords = [
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
]
shading_values = [
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
]

process_test_case(4, transparent, transparency, is_cube, glass, translucent, colliders, vertex_positions, tex_coords, shading_values)



"""
expected value:
Test Case 1:
Transparent: True
Transparency: 2
Is Cube: False
Glass: False
Translucent: False
Colliders: []
Vertex Positions: [[-0.3536, 0.5, 0.3536, -0.3536, -0.5, 0.3536, 0.3536, -0.5, -0.3536, 0.3536, 0.5, -0.3536], [-0.3536, 0.5, -0.3536, -0.3536, -0.5, -0.3536, 0.3536, -0.5, 0.3536, 0.3536, 0.5, 0.3536], [0.3536, 0.5, -0.3536, 0.3536, -0.5, -0.3536, -0.3536, -0.5, 0.3536, -0.3536, 0.5, 0.3536], [0.3536, 0.5, 0.3536, 0.3536, -0.5, 0.3536, -0.3536, -0.5, -0.3536, -0.3536, 0.5, -0.3536]]
Texture Coordinates: [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0]]
Shading Values: [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]

Test Case 2:
Transparent: False
Transparency: 0
Is Cube: True
Glass: False
Translucent: False
Colliders: []
Vertex Positions: [[-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5], [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5], [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5], [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5]]
Texture Coordinates: [[0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]]
Shading Values: [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]

Test Case 3:
Transparent: True
Transparency: 1
Is Cube: True
Glass: True
Translucent: False
Colliders: [[-0.5, -0.5, -0.5, 0.5, 0.5, 0.5]]
Vertex Positions: [[-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5], [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5], [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5], [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5]]
Texture Coordinates: [[0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]]
Shading Values: [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]

Test Case 4:
Transparent: False
Transparency: 0
Is Cube: True
Glass: False
Translucent: True
Colliders: []
Vertex Positions: [[-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5], [-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5], [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5], [-0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5]]
Texture Coordinates: [[0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]]
Shading Values: [[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]
"""
