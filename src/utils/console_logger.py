import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ConsoleLogger:
    __logs = []

    @staticmethod
    def log(msg):
        print(msg)
        ConsoleLogger.__logs.append(msg)

    @staticmethod
    def get_logs():
        return ConsoleLogger.__logs

    @staticmethod
    def clear_logs():
        ConsoleLogger.__logs = []
    
    @staticmethod
    def print_logs():
        for log in ConsoleLogger.__logs:
            print(log)