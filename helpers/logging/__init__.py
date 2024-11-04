import logging


# Logging
logger = logging

# fileHandler = logging.FileHandler("helloflask.log", mode='w')
fileHandler = logging.RotatingFileHandler(
    "my_log.log", maxBytes=2000, backupCount=10)
consoleHandler = logging.StreamHandler()

logger.basicConfig(level=logging.INFO,
                   format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                   handlers=[fileHandler, consoleHandler])
stream_handler = [h for h in logger.root.handlers if isinstance(
    h, logger.StreamHandler)][0]
stream_handler.setLevel(logger.INFO)