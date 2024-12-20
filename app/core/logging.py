import logging
import os
import sys


def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()  # Default to INFO if not set
    logger = logging.getLogger("uvicorn")
    logger.setLevel(log_level)

    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # Console handler to output logs to stdout
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(console_handler)

    return logger
