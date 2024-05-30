import unittest
from lab_5_2 import rand_list


class TestRandList(unittest.TestCase):
    def test_rand_list(self):
        a = []
        f = []
        self.assertEqual(rand_list(a, f), 0)

        a = [100]
        f = []
        self.assertEqual(rand_list(a, f), 100)


if __name__ == '__main__':
    unittest.main()
