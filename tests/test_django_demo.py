from src.example_package.example import add_one

import unittest

class Test_add_one(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(1), 2)
