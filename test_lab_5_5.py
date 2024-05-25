import unittest
from lab_5_5 import fibonaci


class TestFibonaci(unittest.TestCase):
    def test_fibonaci(self):
        self.assertEqual(fibonaci(5), 5)
        self.assertEqual(fibonaci(8), 21)


if __name__ == '__main__':
    unittest.main()
