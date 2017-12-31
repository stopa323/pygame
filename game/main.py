import logging


from game.renderer.game_loop import GameLoop

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)


def main():
    LOG.info("main() func")

    loop = GameLoop()
    loop.run()

if __name__ == '__main__':
    main()
