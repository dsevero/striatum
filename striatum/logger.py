import logging
import os

log_level = getattr(logging, os.getenv('LOG_LEVEL', 'DEBUG'))
fmt = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
logging.basicConfig(level=log_level, format=fmt)


def make_logger(file_: str = 'NO_FILE') -> logging.Logger:
    return logging.getLogger(file_.split("/")[-1])
