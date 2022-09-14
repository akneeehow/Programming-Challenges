import unittest

from Challenge1 import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(meters(10), 50.292)


if __name__ == '__main__':
    unittest.main()
