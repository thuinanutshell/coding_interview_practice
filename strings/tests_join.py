import unittest
from string_join import join_string


class TestJoinString(unittest.TestCase):
    def test_join_with_space(self):
        arr = ["join", "by", "space"]
        s = " "
        st = join_string(arr, s)
        self.assertEqual(st, "join by space")

    def test_join_with_char(self):
        arr = ["b", "", "k", "", "p", "r n", "", "d", "d!!"]
        s = "ee"
        st = join_string(arr, s)
        self.assertEqual(st, "beeeekeeeepeer neeeedeed!!")

    def test_empty_array(self):
        arr = []
        s = "x"
        st = join_string(arr, s)
        self.assertEqual(st, "")

    def test_special_char(self):
        arr = ["tab", "separated"]
        s = "\t"
        st = join_string(arr, s)
        self.assertEqual(st, "tab\tseparated")


if __name__ == "__main__":
    unittest.main()
