import pyglet
from pyglet.graphics import Batch
from pyglet.gl import *

class UpdatedBatch(Batch):
    """
    An extension of the pyglet.graphics.Batch class with additional features.

    @note Contracts:
    - Preconditions:
        None
    - Postconditions:
        - The vertex and color data can be added and cleared from the batch.
        - The batch can be used to render graphics using the provided vertex data and rendering mode.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the UpdatedBatch object.

        @param[in] *args: Variable-length arguments.
        @param[in] **kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)

        self.vertices = []
        self.colors = []
        self.vertex_lists = []

    def add(self, n, mode, group=None, *vertex_lists):
        """
        Adds vertex data to the batch.

        @param[in] n (int): Number of vertices.
        @param[in] mode (int): Rendering mode.
        @param[in] group (Group): Rendering group.
        @param[in] *vertex_lists: Variable-length argument containing vertex lists.

        @note The format of each vertex list should be specified using the first element (e.g., 'v2f' for 2D vertices).
        @note The data of each vertex list should be provided as the second element.

        @note Example:
        @code{python}
        batch.add(4, pyglet.gl.GL_QUADS, None, ('v2f', [0, 0, 100, 0, 100, 100, 0, 100]), ('c3B', [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0]))
        @endcode

        @note Contracts:
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

        @note Contracts:
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

        @note Contracts:
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

        @param[in] n (int): Number of vertices.
        @param[in] mode (int): Rendering mode.
        @param[in] group (Group): Rendering group.
        @param[in] indices (list): List of indices.
        @param[in] *vertex_lists: Variable-length argument containing vertex lists.

        @note The format of each vertex list should be specified using the first element (e.g., 'v2f' for 2D vertices).
        @note The data of each vertex list should be provided as the second element.

        @note Example:
        @code{python}
        batch.add_indexed(4, pyglet.gl.GL_QUADS, None, [0, 1, 2, 3], ('v2f', [0, 0, 100, 0, 100, 100, 0, 100]), ('c3B', [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0]))
        @endcode

        @note Contracts:
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
