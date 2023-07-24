import pyglet
from pyglet.gl import *
from math import sin, cos, pi


"""
Sun settings
"""
SUN_RADIUS = 3
SUN_POSITION = (10, 10, 10)

    
"""
Vertex data for a simple textured sphere
"""
sphere_vertex_list = pyglet.graphics.vertex_list(0, ('v3f', []))


def create_sphere(radius, slices, stacks):
    vertices = []
    for stack in range(stacks + 1):
        for slice in range(slices):
            x = radius * cos(2 * pi * slice / slices) * sin(pi * stack / stacks)
            y = radius * sin(-pi / 2 + pi * stack / stacks)
            z = radius * sin(2 * pi * slice / slices) * sin(pi * stack / stacks)
            vertices.extend([x, y, z])
    return pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices))


def update(dt):
    pass


def draw_sun():
    glPushMatrix()
    glTranslatef(*SUN_POSITION)
    sphere_vertex_list.draw(GL_POINTS)
    glPopMatrix()


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()


    """
    Draw the sun
    """
    draw_sun()


if __name__ == "__main__":
    
    # Load a texture for the sun (you can use your own texture)
    #sun_texture = pyglet.image.load('path/to/your/sun_texture.png').get_texture()

    """
    Set up the sun's vertex data
    """
    sphere_vertex_list = create_sphere(SUN_RADIUS, slices=30, stacks=30)
    draw()

