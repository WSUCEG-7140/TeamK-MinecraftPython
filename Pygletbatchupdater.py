import pyglet
from pyglet.graphics import Batch
from pyglet.gl import *

class UpdatedBatch(Batch):
    """
    An extension of the pyglet.graphics.Batch class with additional features.

    Contracts:
    - Preconditions:
        None
    - Postconditions:
        - The vertex and color data can be added and cleared from the batch.
        - The batch can be used to render graphics using the provided vertex data and rendering mode.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the UpdatedBatch object.

        Args:
            *args: Variable-length arguments.
            **kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)

        self.vertices = []
        self.colors = []
        self.vertex_lists = []

    def add(self, n, mode, group=None, *vertex_lists):
        """
        Adds vertex data to the batch.

        Args:
            n (int): Number of vertices.
            mode (int): Rendering mode.
            group (Group): Rendering group.
            *vertex_lists: Variable-length argument containing vertex lists.

        Note:
            - The format of each vertex list should be specified using the first element (e.g., 'v2f' for 2D vertices).
            - The data of each vertex list should be provided as the second element.

        Example:
            batch.add(4, pyglet.gl.GL_QUADS, None, ('v2f', [0, 0, 100, 0, 100, 100, 0, 100]), ('c3B', [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0]))

        Contracts:
        - Preconditions:
            None
        - Postconditions:
            - Vertex data is added to the batch.
            - The 'vertices' and 'colors' attributes are updated accordingly.
        """
        vertex_format = ''
        for vl in vertex_lists:
            vertex_format += vl[0]

        vertices = []
        colors = []
        for vl in vertex_lists:
            data = vl[1]
            if vl[0] == 'v2f':
                vertices.extend(data)
            elif vl[0] == 'c3B' or vl[0] == 'c4B' or vl[0] == 't3B':
                colors.extend(data)

        self.vertices.extend(vertices)
        self.colors.extend(colors)

    def delete(self):
        """
        Deletes the vertex and color data from the batch.

        Contracts:
        - Preconditions:
            None
        - Postconditions:
            - The 'vertices' and 'colors' attributes are cleared.
        """
        self.vertices = []
        self.colors = []

    def clear(self):
        """
        Clears the vertex and color data from the batch.

        Contracts:
        - Preconditions:
            None
        - Postconditions:
            - The 'vertices' and 'colors' attributes are cleared.
        """
        self.vertices = []
        self.colors = []

    def add_indexed(self, n, mode, group, indices, *vertex_lists):
        """
        Adds indexed vertex data to the batch.

        Args:
            n (int): Number of vertices.
            mode (int): Rendering mode.
            group (Group): Rendering group.
            indices (list): List of indices.
            *vertex_lists: Variable-length argument containing vertex lists.

        Note:
            - The format of each vertex list should be specified using the first element (e.g., 'v2f' for 2D vertices).
            - The data of each vertex list should be provided as the second element.

        Example:
            batch.add_indexed(4, pyglet.gl.GL_QUADS, None, [0, 1, 2, 3], ('v2f', [0, 0, 100, 0, 100, 100, 0, 100]), ('c3B', [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0]))

        Contracts:
        - Preconditions:
            None
        - Postconditions:
            - Indexed vertex data is added to the batch.
            - The 'vertices' and 'colors' attributes are updated accordingly.
        """
        vertex_format = ''
        for vl in vertex_lists:
            vertex_format += vl[0]

        vertices = []
        colors = []
        for vl in vertex_lists:
            data = vl[1]
            if vl[0] == 'v2f':
                vertices.extend(data)
            elif vl[0] == 'c3B' or vl[0] == 'c4B' or vl[0] == 't3B':
                colors.extend(data)

        self.vertices.extend(vertices)
        self.colors.extend(colors)
