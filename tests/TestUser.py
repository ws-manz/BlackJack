import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.game.user import User

class TestUser(unittest.TestCase):

    def test_create_user(self):
        user = User("Jane","jane")
        self.assertEqual(user.name, "Jane")
        #self.assertEqual(user.wallet, 100)

    def test_username(self):
        user = User("Jane","jane")
        self.assertEqual(user.username, "jane")
        #self.assertEqual(user.wallet, 100)
        
    '''def test_add_funds(self):
        user = User("Jane")
        user.add_funds(50)
        self.assertEqual(user.wallet, 150)

    def test_withdraw_funds(self):
        user = User("Jane")
        user.withdraw_funds(50)
        self.assertEqual(user.wallet, 50)

    def test_insufficient_funds(self):
        user = User("Jane")
        with self.assertRaises(ValueError):
            user.withdraw_funds(150)'''

if __name__ == '__main__':
    unittest.main()