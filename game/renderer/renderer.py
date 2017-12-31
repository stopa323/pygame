from OpenGL.GL import *
from OpenGL.raw.GL.VERSION.GL_3_0 import glBindVertexArray


class Renderer(object):

    @classmethod
    def prepare(cls):
        glClearColor(0.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    @classmethod
    def render_model(cls, model):
        glBindVertexArray(model.vao_id)
        glEnableVertexAttribArray(0)
        glDrawElements(GL_TRIANGLES, model.vertex_count, GL_UNSIGNED_INT, None)
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)
