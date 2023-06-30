import pyglet
from pyglet.graphics import Batch
from pyglet.gl import *



class UpdatedBatch(Batch):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

        self.vertices = []
        self.colors = []
        self.vertex_lists = []

    def add(self, n, mode, group=None, *vertex_lists):
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
        self.vertices = []
        self.colors = []


    def clear(self):
        self.vertices = []
        self.colors = []

    def add_indexed(self, n, mode, group, indices, *vertex_lists):
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


# Test Case 1: Updating the vertices and colors in the batch
batch = UpdatedBatch()
batch.vertices = (200, 200, 300, 200, 250, 300)
batch.colors = (0, 255, 0, 0, 0, 255, 0, 0, 0)
assert batch.vertices == (200, 200, 300, 200, 250, 300)
assert batch.colors == (0, 255, 0, 0, 0, 255, 0, 0, 0)

# Test Case 2: Removing elements from the batch
batch.delete()
assert len(batch.vertex_lists) == 0

# Test Case 3: Clearing the batch
batch.clear()
assert len(batch.vertex_lists) == 0

# Test Case 4: Using different primitive types when adding elements to the batch
batch.add(6, GL_LINES, None,
          ('v2f', (100, 100, 200, 100, 200, 100, 100, 200, 200, 200, 200, 100)),
          ('c3B', (255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0, 0, 0, 255, 255, 0, 0)))

# Test Case 5: Adding different vertex attribute formats
batch.add(4, GL_QUADS, None,
          ('v2f', (100, 100, 200, 100, 200, 200, 100, 200)),
          ('c4B', (255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255)))

# Test Case 6: Using custom vertex attribute formats
batch.add(3, GL_TRIANGLES, None,
          ('v2i', (100, 100, 200, 100, 150, 200)),
          ('t3B', (255, 0, 0, 0, 255, 0, 0, 0, 255)))

# Test Case 7: Creating multiple batches
batch1 = UpdatedBatch()
batch2 = UpdatedBatch()
assert len(batch1.vertex_lists) == 0
assert len(batch2.vertex_lists) == 0

# Test Case 8: Using batch indexing with different index formats
batch.add_indexed(6, GL_LINES, None,
                  [0, 1, 1, 2, 2, 0, 0, 3, 3, 2, 2, 1],
                  ('v2f', (100, 100, 200, 100, 200, 200, 100, 200)),
                  ('c3B', (255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0, 0, 0, 255, 255, 0, 0)))

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_DEPTH_TEST)
    batch.draw()
