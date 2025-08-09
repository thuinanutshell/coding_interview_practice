from typing import List
import unittest
from copy import deepcopy


def set_zero(arr, r, c, row_len, col_len):
    for i in range(row_len):
        arr[i][c] = 0

    for j in range(col_len):
        arr[r][j] = 0

    return arr


def set_zero_matrix(arr):
    col_len = len(arr[0])
    row_len = len(arr)
    new_matrix = deepcopy(arr)

    for r in range(row_len):
        for c in range(col_len):
            if arr[r][c] == 0:
                new_matrix = set_zero(deepcopy(arr), r, c, row_len, col_len)

    return new_matrix


class TestSetZeroMatrix(unittest.TestCase):
    def test_case(self):
        arr = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
        matrix = set_zero_matrix(arr)
        self.assertEqual(matrix, [[0, 0, 0, 0], [0, 5, 6, 7], [0, 9, 10, 11]])


if __name__ == "__main__":
    unittest.main()
