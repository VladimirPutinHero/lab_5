import unittest
from lab_5_4 import check_anagrams


class TestCheckAnagrams(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(check_anagrams(["listen", "silent"]))
        self.assertTrue(check_anagrams(["hello", "llohe"]))
        self.assertFalse(check_anagrams(["apple", "orange"]))


if __name__ == '__main__':
    unittest.main()
