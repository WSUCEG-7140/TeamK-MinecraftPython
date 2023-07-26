"""
TESTS for clouds.py
https://github.com/WSUCEG-7140/TeamK-MinecraftPython/issues/51
"""

from clouds import *


import pyglet
from pyglet.gl import *
from random import randint
from math import sin, cos, pi


''' 
Sample test case to ensure working PyTest
'''
def test_pytest():
    assert True

 
"""
Test: create the clouds' vertex data
"""
def create_cloud(radius, slices, stacks):

    """
    Pass: if radius is > 0
    """
    assert radius > 0, 'radius is not greater than 0!'


    """
    Pass: if slices is > 0
    """
    assert slices > 0, 'slices is not greater than 0!'


    """
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
    Pass: if list vertices is not empty
    """ 
    assert vertices is not None, 'vertices is empty!'

    create_clouds(pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices)))


"""
Test: create cloud positions
"""
def create_clouds(sphere_vertex_list):

    """
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'

    CLOUD_HEIGHT = 20
    NUM_CLOUDS = 30
    CLOUD_TEXTURE_PATH = 'cloud_texture.png'


    """
    Pass: if path to CLOUD_TEXTURE_PATH is not empty
    """ 
    assert CLOUD_TEXTURE_PATH is not None , 'CLOUD_TEXTURE_PATH is empty!'

    clouds = []

    """
    Load the cloud texture
    """
    cloud_image = pyglet.image.load(CLOUD_TEXTURE_PATH)
    cloud_texture = cloud_image.get_texture()


    """
    Pass: if cloud_texture is not empty
    """ 
    assert cloud_texture is not None, 'cloud_texture is empty!'

    glBindTexture(GL_TEXTURE_2D, cloud_texture.id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    for _ in range(NUM_CLOUDS):
        x = randint(-40, 40)
        y = randint(CLOUD_HEIGHT, - 5, CLOUD_HEIGHT + 5)
        z = randint(-40, 40)
        clouds.append((x, y, z))


    """
    Pass: if list clouds is not empty
    """ 
    assert clouds is not None, 'clouds is empty!'


    """
    Pass: if each element in list clouds is numerical
    """ 
    for coordinates in clouds:
        for coordinate in coordinates:
            coordinate_float = float(coordinate)
            assert isinstance(coordinate_float, float), 'clouds contains a non-numerical value!'

    draw(sphere_vertex_list, clouds, cloud_texture)


"""
Test: enable buffer to draw
"""
def draw(sphere_vertex_list, clouds, cloud_texture):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()


    """
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'


    """
    Pass: if list clouds is not empty
    """ 
    assert clouds is not None, 'clouds is empty!'


    """
    Pass: if cloud_texture is not empty
    """ 
    assert cloud_texture is not None, 'cloud_texture is empty!'

    draw_clouds(sphere_vertex_list, clouds, cloud_texture)


"""
Test: draw the clouds
"""
def draw_clouds(sphere_vertex_list, clouds, cloud_texture):

    """
    Pass: if list sphere_vertex_list is not empty
    """ 
    assert sphere_vertex_list is not None, 'sphere_vertex_list is empty!'


    """
    Pass: if list clouds is not empty
    """ 
    assert clouds is not None, 'clouds is empty!'


    """
    Pass: if cloud_texture is not empty
    """ 
    assert cloud_texture is not None, 'cloud_texture is empty!'

    glBindTexture(GL_TEXTURE_2D, cloud_texture.id)
    glColor4f(1, 1, 1, 1)

    for cloud in clouds:
        glPushMatrix()
        glTranslatef(*cloud)
        sphere_vertex_list.draw(GL_POINTS)
        glPopMatrix()

