from dynamic_array import DynamicArray
import unittest


class TestDynamicArray(unittest.TestCase):
    def test_append_and_get(self):
        da = DynamicArray()
        da.append(1)
        da.append(2)
        da.append(3)
        self.assertEqual(da.size, 3)
        self.assertEqual(da.get(0), 1)
        self.assertEqual(da.get(1), 2)
        self.assertEqual(da.get(2), 3)

    def test_set(self):
        da = DynamicArray()
        da.append(5)
        da.set(0, 10)
        self.assertEqual(da.get(0), 10)

    def test_pop_back(self):
        da = DynamicArray()
        da.append(1)
        da.append(2)
        popped = da.pop_back()
        self.assertEqual(popped, 2)
        self.assertEqual(da.size, 1)

    def test_contain(self):
        da = DynamicArray()
        da.append(1)
        da.append(2)
        boolean1 = da.contains(1)
        boolean2 = da.contains(3)
        self.assertEqual(boolean1, True)
        self.assertEqual(boolean2, False)

    def test_insert(self):
        da = DynamicArray()
        da.append(1)
        da.append(2)
        da.append(3)
        da.insert(1, 4)
        self.assertEqual(da.arr[: da.size], [1, 4, 2, 3])

    def test_remove(self):
        da = DynamicArray()
        da.append(1)
        da.append(2)
        da.append(3)
        removed = da.remove(3)
        self.assertEqual(removed, 2)

    def test_pop(self):
        da = DynamicArray()
        da.append(1)
        da.append(2)
        da.append(3)
        popped = da.pop(0)
        self.assertEqual(popped, 1)

    def test_out_of_bounds(self):
        da = DynamicArray()
        da.append(1)
        with self.assertRaises(IndexError):
            da.get(5)
        with self.assertRaises(IndexError):
            da.set(5, 10)
        da.pop_back()
        with self.assertRaises(IndexError):
            da.pop_back()


if __name__ == "__main__":
    unittest.main()
