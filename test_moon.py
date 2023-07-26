"""
TESTS for clouds.py
https://github.com/WSUCEG-7140/TeamK-MinecraftPython/issues/53
"""


from moon import *


import pyglet
from pyglet.gl import *
from math import sin, cos, pi


''' 
Sample test case to ensure working PyTest
'''
def test_pytest():
    assert True


"""
Test: create vertex data for a simple textured sphere
"""
def create_moon(radius, slices, stacks):

    """
    @param[in]
    Pass: if radius is > 0
    """
    assert radius > 0, 'radius is not greater than 0!'


    """
    @param[in]
    Pass: if slices is > 0
    """
    assert slices > 0, 'slices is not greater than 0!'


    """
    @param[in]
    Pass: if stacks is > 0
    """
    assert stacks > 0, 'stacks is not greater than 0!'
    
    vertices = []

    for stack in range(stacks + 1):
        for slice in range(slices):
            x = radius * cos(2 * pi * slice / slices) * sin(pi * stack / stacks)
            y = radius * sin(-pi / 2 + pi * stack / stacks)
            z = radius * sin(2 * pi * slice / slices) * sin(pi * stack / stacks)
            vertices.extend([x, y, z])


    """
    @param[out]
    Pass: if list vertices is not empty
    """ 
    assert vertices is not None, 'vertices is empty!'


    """
    @param[out]
    Pass: if each element in list vertices is numerical
    """ 
    for coordinates in vertices:
        for coordinate in coordinates:
            coordinate_float = float(coordinate)
            assert isinstance(coordinate_float, float), 'vertices contains a non-numerical value!'

    draw(pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices)))


"""
Test: enable buffer to draw
"""
def draw(sphere_vertex_list):

    """
    @param[in]
    @param[out]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_moon(sphere_vertex_list)


"""
Test: draw the moon
"""
def draw_moon(sphere_vertex_list):

    """
    @param[in]
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    MOON_POSITION = (0, 15, -15)

    glPushMatrix()
    glTranslatef(*MOON_POSITION)
    sphere_vertex_list.draw(GL_POINTS)
    glPopMatrix()

