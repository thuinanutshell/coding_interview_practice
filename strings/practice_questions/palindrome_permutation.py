import unittest


def is_palindrome_permutation(s: str) -> bool:
    s.lower()
    n = len(set(s))

    if n == 1:
        return True
    else:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        freq_list = set(freq.values())

        # length is even
        if n % 2 == 0:
            if len(freq_list) == 1:
                return True
            elif len(freq_list) == len(freq):
                return True
            else:
                return False

        # length is odd
        else:
            odd_freqs = 0
            for val in freq_list:
                if val % 2 == 1:
                    odd_freqs += 1
            if odd_freqs > 1:
                return False
            else:
                return True


class TestPalindromePermutation(unittest.TestCase):
    def test_one_odd_all_even(self):
        s = "Taco Cat"
        boolean = is_palindrome_permutation(s)
        self.assertEqual(boolean, True)

    def test_all_same_char(self):
        s = "CCC"
        boolean = is_palindrome_permutation(s)
        self.assertEqual(boolean, True)

    def test_even_same_freq(self):
        s = "aabbcc"  # abccba -> abccba
        boolean = is_palindrome_permutation(s)
        self.assertEqual(boolean, True)

    def test_even_not_same_freq(self):
        s = "aabbbbcc"  # abbccbba -> abbccbba
        boolean = is_palindrome_permutation(s)
        self.assertEqual(boolean, True)

    def test_two_odds_all_even(self):
        s = "aabcdd"
        boolean = is_palindrome_permutation(s)
        self.assertEqual(boolean, False)


if __name__ == "__main__":
    unittest.main()
