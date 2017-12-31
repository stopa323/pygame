import glfw
import logging
import numpy as np
import OpenGL.GL.shaders as shaders
import pyrr

from OpenGL.GL import *


logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)


def main():
    if not glfw.init():
        LOG.error("Could not initialize GLFW")
        return

    window = glfw.create_window(800, 600, "Title", None, None)
    if not window:
        LOG.error("Could not create window")
        return

    glfw.make_context_current(window)

    quad = np.array([
        0.5, 0.5, 0.5, 1.0, 0.0, 0.0,
        0.5, -0.5, 0.5, 0.0, 1.0, 0.0,
        -0.5, -0.5, 0.5, 0.0, 0.0, 1.0,
        -0.5, 0.5, 0.5, 0.0, 0.0, 0.0,
        0.5, 0.5, -0.5, 1.0, 0.0, 0.0,
        0.5, -0.5, -0.5, 0.0, 1.0, 0.0,
        -0.5, -0.5, -0.5, 0.0, 0.0, 1.0,
        -0.5, 0.5, -0.5, 0.0, 0.0, 0.0],
        dtype=np.float32)

    indices = np.array([
        0, 1, 2, 2, 3, 0,
        4, 5, 6, 6, 7, 4,
        4, 5, 1, 1, 0, 4,
        3, 2, 6, 6, 7, 3,
        1, 2, 6, 6, 5, 1,
        0, 3, 7, 7, 4, 0], dtype=np.uint32)

    vtx_shader = """
    #version 330
    
    in vec3 position;
    in vec3 color;
    
    uniform mat4 transform;
    
    out vec3 newColor;
    
    void main(){
        gl_Position = transform * vec4(position, 1.0f);
        newColor = color;
    }
    """

    frag_shader = """
    #version 330
    
    in vec3 newColor;
    
    out vec4 outColor;
    void main(){
        outColor = vec4(newColor, 1.0f);
    }
    """

    shader = shaders.compileProgram(
        shaders.compileShader(vtx_shader, GL_VERTEX_SHADER),
        shaders.compileShader(frag_shader, GL_FRAGMENT_SHADER))

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 192, quad, GL_STATIC_DRAW)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 144, indices, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shader, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)

    glUseProgram(shader)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        rot_x = pyrr.Matrix44.from_x_rotation(np.pi * glfw.get_time())
        rot_y = pyrr.Matrix44.from_y_rotation(np.pi * glfw.get_time())

        transform_loc = glGetUniformLocation(shader, "transform")
        glUniformMatrix4fv(transform_loc, 1, GL_FALSE, rot_x * rot_y)

        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == '__main__':
    main()
