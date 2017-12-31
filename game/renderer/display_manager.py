import glfw
import logging

from game.renderer import exceptions

LOG = logging.getLogger(__name__)


class DisplayManager(object):

    def __init__(self, width=600, height=400, title="Test title"):
        self._width = width
        self._height = height
        self._title = title

        if not glfw.init():
            raise exceptions.InitializationException(
                "GLFW could not be initialized")
        LOG.info("GLFW initialized")

        self._window = glfw.create_window(self._width, self._height,
                                          self._title, None, None)
        if not self._window:
            raise exceptions.InitializationException("Could not create window")
        LOG.debug("Created window=(%s, %s, %s)" %
                  (self._width, self._height, self._title))

        glfw.make_context_current(self._window)

    def should_close_window(self):
        return glfw.window_should_close(self._window)

    def swap_buffers(self):
        # TODO: rethink
        glfw.swap_buffers(self._window)

    @classmethod
    def poll_events(cls):
        # TODO: rethink
        glfw.poll_events()

    @classmethod
    def close_window(cls):
        glfw.terminate()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def title(self):
        return self._title
