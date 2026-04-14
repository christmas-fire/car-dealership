import sys
from loguru import logger


def setup_logging():
    logger.remove()

    format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> - "
        "<level>{level}</level> - "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
    )

    logger.add(sys.stderr, level="DEBUG", format=format, colorize=True)
    