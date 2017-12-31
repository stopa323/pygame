import logging

from game.renderer.display_manager import DisplayManager

LOG = logging.getLogger(__name__)


class GameLoop(object):

    def __init__(self):
        self._display_manager = DisplayManager()

    def run(self):
        LOG.debug("Starting main game loop")

        while not self._display_manager.should_close_window():
            self._display_manager.poll_events()
            self._display_manager.swap_buffers()

        self._display_manager.close_window()
