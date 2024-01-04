import logging
from logging.handlers import RotatingFileHandler
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_LOG = ROOT + "/logs/etl.log"

def create_folder(path: str) -> bool:
    """Create a folder if it doesn't exist."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return True


def create_loger() -> logging.Logger:
    """Create a loger for the ETL process."""
    # Create a custom logger
    logger = logging.getLogger('ETL-CDE')
    logger.setLevel(logging.INFO)

    create_folder(PATH_LOG)

    # Create handlers
    handler = RotatingFileHandler(PATH_LOG, maxBytes=100*1024*1024, backupCount=3)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(handler)

    return logger

