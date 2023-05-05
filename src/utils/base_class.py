import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.console_logger import ConsoleLogger

class BaseClass:
    logger = ConsoleLogger()

    def __init__(self):
        pass