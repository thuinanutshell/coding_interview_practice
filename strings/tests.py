import unittest
from string_split import split_string


class TestSplitString(unittest.TestCase):
    def test_split_with_space(self):
        s = "split by space"
        c = " "
        arr = split_string(s, c)
        self.assertEqual(arr, ["split", "by", "space"])

    def test_split_with_char(self):
        s = "beekeeper needed"
        c = "e"
        arr = split_string(s, c)
        self.assertEqual(arr, ["b", "", "k", "", "p", "r n", "", "d", "d"])

    def test_split_with_slash(self):
        s = "/home/./..//Documents/"
        c = "/"
        arr = split_string(s, c)
        self.assertEqual(arr, ["", "home", ".", "..", "", "Documents", ""])

    def test_split_with_empty_string(self):
        s = ""
        c = "?"
        arr = split_string(s, c)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
