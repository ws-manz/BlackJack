import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.object_value.gender import Gender

BOTS = []

with open('../src/files/asserts/bots.txt', 'r') as file:
    for line in file:
        name, gender = line.strip().split(',')
        BOTS.append((name, Gender[gender.strip().upper()]))
        
class TestBotFile(unittest.TestCase):
    def test_bot_file_reading(self):
        self.assertEqual(len(BOTS), 25)  # assumes there are 3 lines in the file
    
    def test_bot_name_fist_line(self):        
        self.assertEqual(BOTS[0][0], "Alice")
        print(BOTS[0][1])
        self.assertEqual(BOTS[0][1], Gender.FEMALE)

if __name__ == '__main__':
    unittest.main()
