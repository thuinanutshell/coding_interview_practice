from dynamic_array import DynamicArray


def test_dynamic_array():
    da = DynamicArray()

    # Test append and size
    da.append(10)
    da.append(20)
    da.append(30)
    assert da.size == 3, f"Expected size 3, got {da.size}"
    assert da.get(0) == 10
    assert da.get(1) == 20
    assert da.get(2) == 30

    # Test set
    da.set(1, 25)
    assert da.get(1) == 25

    # Test pop_back
    val = da.pop_back()
    assert val == 30
    assert da.size == 2

    # Test out-of-bounds access
    try:
        da.get(5)
        assert False, "Expected IndexError"
    except IndexError:
        pass

    try:
        da.set(5, 100)
        assert False, "Expected IndexError"
    except IndexError:
        pass

    try:
        empty_da = DynamicArray()
        empty_da.pop_back()
        assert False, "Expected IndexError on pop_back"
    except IndexError:
        pass

    print("All tests passed!")


test_dynamic_array()
