import logging

from abc import abstractmethod, abstractclassmethod
from OpenGL.GL import *
from OpenGL.GL.VERSION.GL_2_0 import glShaderSource
from OpenGL.GL.shaders import glDetachShader

LOG = logging.getLogger(__name__)


class ShaderProgramBase(object):

    def __init__(self, vertex_shader_path, fragment_shader_path):
        self._vertex_shader_id = self._load_shader(vertex_shader_path,
                                                   GL_VERTEX_SHADER)
        self._fragment_shader_id = self._load_shader(fragment_shader_path,
                                                     GL_FRAGMENT_SHADER)
        self._program_id = glCreateProgram()
        glAttachShader(self._program_id, self._vertex_shader_id)
        glAttachShader(self._program_id, self._fragment_shader_id)
        self._bind_attribs()
        glLinkProgram(self._program_id)
        glValidateProgram(self._program_id)

    def start(self):
        glUseProgram(self._program_id)

    def stop(self):
        glUseProgram(0)

    def clean_up(self):
        LOG.debug("Cleaning shader program: %s" % self._program_id)
        self.stop()
        glDetachShader(self._program_id, self._vertex_shader_id)
        glDetachShader(self._program_id, self._fragment_shader_id)
        glDeleteShader(self._vertex_shader_id)
        glDeleteShader(self._fragment_shader_id)
        glDeleteProgram(self._program_id)

    @abstractclassmethod
    def _bind_attribs(self):
        pass

    def _bind_attrib(self, attr_num, var_name):
        glBindAttribLocation(self._program_id, attr_num, var_name)

    @classmethod
    def _load_shader(cls, path, shader_type):
        LOG.info("Loading shader: %s" % path)
        with open(path) as source:
            shader_id = glCreateShader(shader_type)
            glShaderSource(shader_id, source.readlines())
            glCompileShader(shader_id)

            if glGetShaderiv(shader_id, GL_COMPILE_STATUS) != GL_TRUE:
                raise RuntimeError("Shader compilation failed")

            return shader_id


class StaticShader(ShaderProgramBase):

    VERTEX_FILE = "./shaders/vertexShader.txt"
    FRAGMENT_FILE = "./shaders/fragmentShader.txt"

    def __init__(self):
        super(StaticShader, self).__init__(StaticShader.VERTEX_FILE,
                                           StaticShader.FRAGMENT_FILE)

    def _bind_attribs(self):
        self._bind_attrib(0, "position")
