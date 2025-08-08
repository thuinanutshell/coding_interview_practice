import unittest
from string_match import index_of


class TestJoinString(unittest.TestCase):
    def test_match_space(self):
        s = "hello world"
        t = "world"
        idx = index_of(s, t)
        self.assertEqual(idx, 6)


if __name__ == "__main__":
    unittest.main()
