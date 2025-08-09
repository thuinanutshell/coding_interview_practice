import unittest


def is_one_away(s1: str, s2: str) -> bool:
    row_len = len(s1)
    col_len = len(s2)

    dp = [[0] * (col_len + 1) for _ in range(row_len + 1)]

    for col in range(col_len + 1):
        dp[0][col] = col

    for row in range(row_len + 1):
        dp[row][0] = row

    for i in range(1, row_len + 1):
        for j in range(1, col_len + 1):
            if s1[i - 1] != s2[j - 1]:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # above row
                    dp[i][j - 1],  # left col
                    dp[i - 1][j - 1],  # top left
                )
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    if dp[row_len][col_len] == 1:
        return True
    else:
        return False


class TestOneEditAway(unittest.TestCase):
    def test_one_delete(self):
        s1 = "pale"
        s2 = "ple"
        boolean = is_one_away(s1, s2)
        self.assertEqual(boolean, True)

    def test_one_delete2(self):
        s1 = "pales"
        s2 = "pale"
        boolean = is_one_away(s1, s2)
        self.assertEqual(boolean, True)

    def test_one_replace(self):
        s1 = "pale"
        s2 = "bale"
        boolean = is_one_away(s1, s2)
        self.assertEqual(boolean, True)

    def test_not_one_edit(self):
        s1 = "pale"
        s2 = "bake"
        boolean = is_one_away(s1, s2)
        self.assertEqual(boolean, False)


if __name__ == "__main__":
    unittest.main()
