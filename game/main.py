import glfw
import logging

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

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == '__main__':
    main()
