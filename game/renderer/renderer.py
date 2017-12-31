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
        glDrawArrays(GL_TRIANGLES, 0, model.vertex_count)
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)
