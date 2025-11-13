import logging
from src.config import Config

Conf = Config()

def setup_root_logging():
    DEBUG = Conf.get_log_config()["DEBUG"]
    logger = logging.getLogger("root")
    c_handler = logging.StreamHandler()
    if DEBUG == "True":
        logger.setLevel(logging.DEBUG)
        c_handler.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
        c_handler.setLevel(logging.INFO)
    c_format = logging.Formatter(
        '[%(asctime)s]  %(name)s  %(levelname)s  %(message)s')
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)
