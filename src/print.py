import logging
from src.config import Config

Conf = Config()
logger = logging.getLogger(__name__)


class PrintLOG:

    def __init__(self):
        self._message = Conf.get_print_config()["MESSAGE"]

    def print(self):
        logger.info(self._message)
