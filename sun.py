import pyglet
from pyglet.gl import *
from math import sin, cos, pi


"""
Create vertex data for a simple textured sphere
"""
def create_sun(radius, slices, stacks):
    vertices = []
    for stack in range(stacks + 1):
        for slice in range(slices):
            x = radius * cos(2 * pi * slice / slices) * sin(pi * stack / stacks)
            y = radius * sin(-pi / 2 + pi * stack / stacks)
            z = radius * sin(2 * pi * slice / slices) * sin(pi * stack / stacks)
            vertices.extend([x, y, z])
    draw(pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices)))


"""
Enable buffer to draw
"""
def draw(sphere_vertex_list):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_sun(sphere_vertex_list)
    

"""
Draw the sun
"""
def draw_sun(sphere_vertex_list):
    SUN_POSITION = (10, 10, 10)

    glPushMatrix()
    glTranslatef(*SUN_POSITION)
    sphere_vertex_list.draw(GL_POINTS)
    glPopMatrix()


def update(dt):
    pass

