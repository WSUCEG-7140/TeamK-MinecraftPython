import pyglet
from pyglet.gl import *
from random import randint
from math import sin, cos, pi


"""
Create the clouds' vertex data
"""
def create_cloud(radius, slices, stacks):
    vertices = []
    for stack in range(stacks + 1):
        for slice in range(slices):
            x = radius * cos(2 * pi * slice / slices) * sin(pi * stack / stacks)
            y = radius * sin(-pi / 2 + pi * stack / stacks)
            z = radius * sin(2 * pi * slice / slices) * sin(pi * stack / stacks)
            vertices.extend([x, y, z])
    create_clouds(pyglet.graphics.vertex_list(len(vertices) // 3, ('v3f', vertices)))


"""
Create cloud positions
"""
def create_clouds(sphere_vertex_list):
    CLOUD_HEIGHT = 20
    NUM_CLOUDS = 30
    CLOUD_TEXTURE_PATH = 'cloud_texture.png'
    clouds = []

    """
    Load the cloud texture
    """
    cloud_image = pyglet.image.load(CLOUD_TEXTURE_PATH)
    cloud_texture = cloud_image.get_texture()
    glBindTexture(GL_TEXTURE_2D, cloud_texture.id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    for _ in range(NUM_CLOUDS):
        x = randint(-40, 40)
        y = randint(CLOUD_HEIGHT, - 5, CLOUD_HEIGHT + 5)
        z = randint(-40, 40)
        clouds.append((x, y, z))

    draw(sphere_vertex_list, clouds, cloud_texture)


"""
Enable buffer to draw
"""
def draw(sphere_vertex_list, clouds, cloud_texture):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_clouds(sphere_vertex_list, clouds, cloud_texture)


"""
Draw the clouds
"""
def draw_clouds(sphere_vertex_list, clouds, cloud_texture):
    glBindTexture(GL_TEXTURE_2D, cloud_texture.id)
    glColor4f(1, 1, 1, 1)

    for cloud in clouds:
        glPushMatrix()
        glTranslatef(*cloud)
        sphere_vertex_list.draw(GL_POINTS)
        glPopMatrix()


def update(dt):
    pass


