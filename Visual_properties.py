"""
File: Visual-properties.py

Description: A  code to demonstrate object properties.

"""
# Set transparency-related variables
transparent = True    # Indicates whether the object is transparent  /**< @param[in] transparent: boolean flag indicating if the object is transparent */
transparency = 2      # Transparency level (assumed to be on a scale of 0-10)  /**< @param[in] transparency: integer representing the transparency level on a scale of 0-10 */

# Set object properties
is_cube = False       # Indicates whether the object is a cube  /**< @param[in] is_cube: boolean flag indicating if the object is a cube */
glass = False         # Indicates whether the object is made of glass  /**< @param[in] glass: boolean flag indicating if the object is made of glass */
translucent = False   # Indicates whether the object is translucent  /**< @param[in] translucent: boolean flag indicating if the object is translucent */

colliders = []        # An empty list to store collider objects (if any)  /**< @param[out] colliders: list to store collider objects */

# Define vertex positions for the object
vertex_positions = [
    [-0.3536, 0.5000,  0.3536, -0.3536, -0.5000,  0.3536,  0.3536, -0.5000, -0.3536,  0.3536, 0.5000, -0.3536],
    [-0.3536, 0.5000, -0.3536, -0.3536, -0.5000, -0.3536,  0.3536, -0.5000,  0.3536,  0.3536, 0.5000,  0.3536],
    [ 0.3536, 0.5000, -0.3536,  0.3536, -0.5000, -0.3536, -0.3536, -0.5000,  0.3536, -0.3536, 0.5000,  0.3536],
    [ 0.3536, 0.5000,  0.3536,  0.3536, -0.5000,  0.3536, -0.3536, -0.5000, -0.3536, -0.3536, 0.5000, -0.3536],
]

# Define texture coordinates for the object
tex_coords = [
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0],
]

# Define shading values for the object
shading_values = [
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
]
