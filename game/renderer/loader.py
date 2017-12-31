from game.renderer.model import RawModel
from OpenGL.GL import *


class Loader(object):
    """Load 3D models into memory by storing model data in VAO """

    def __init__(self):
        self._vao_list = list()
        self._vbo_list = list()

    def load_to_vao(self, positions):
        """Load """

        vao_id = self._create_vao()
        self._store_data_in_attr_list(0, positions)
        self._unbind_vao()
        return RawModel(vao_id, len(positions)/3)

    def clean_up(self):
        """Clean all VAOs and VBOs. """
        glDeleteVertexArrays(len(self._vao_list), self._vao_list)
        glDeleteBuffers(len(self._vbo_list), self._vbo_list)

    def _create_vao(self):
        """Create empty new VAO.

        :returns newly created VAO id
        :rtype int
        """
        vao_id = glGenVertexArrays(1)
        self._vao_list.append(vao_id)

        glBindVertexArray(vao_id)
        return vao_id

    def _store_data_in_attr_list(self, attr_num, data):
        """Store data in attribute list of VAO"""
        vbo_id = glGenBuffers(1)
        self._vbo_list.append(vbo_id)

        glBindBuffer(GL_ARRAY_BUFFER, vbo_id)
        glBufferData(GL_ARRAY_BUFFER, data, GL_STATIC_DRAW)
        glVertexAttribPointer(attr_num, 3, GL_FLOAT, GL_FALSE, 0,
                              ctypes.c_void_p(0))
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def _unbind_vao(self):
        glBindVertexArray(0)
