import logging

from game.renderer.display_manager import DisplayManager
from game.renderer.loader import Loader
from game.renderer.renderer import Renderer

LOG = logging.getLogger(__name__)


class GameLoop(object):

    def __init__(self):
        self._display_manager = DisplayManager()
        self._loader = Loader()

    def run(self):
        LOG.debug("Starting main game loop")
        import numpy as np

        quad = np.array(
            [-0.5, 0.5, 0,
             -0.5, -0.5, 0,
             0.5, -0.5, 0,
             0.5, 0.5, 0],
            dtype=np.float32)
        indices = np.array([0, 1, 2, 2, 3, 0], dtype=np.uint32)

        model = self._loader.load_to_vao(quad, indices)

        while not self._display_manager.should_close_window():
            Renderer.prepare()
            Renderer.render_model(model)
            self._display_manager.poll_events()
            self._display_manager.swap_buffers()

        self._loader.clean_up()
        self._display_manager.close_window()
