"""Main module for msticpy extension logic"""

import logging

logger = logging.getLogger(__name__)

logger.info(f"Loading msticpy extension: {__file__}")

def my_extension():
    print("Hi, Ian!")