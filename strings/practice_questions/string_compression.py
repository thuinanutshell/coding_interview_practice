import unittest


def compress_string(s: str):
    output = []
    st = ""

    for char in s:
        if st != "":
            if char == st[-1]:
                st += char
            else:
                output.append(f"{st[-1]}{len(st)}")
                st = char
        else:
            st += char

    if st != "":
        output.append(f"{st[-1]}{len(st)}")

    return "".join(output)


class TestCompressString(unittest.TestCase):
    def test_compress_string(self):
        s = "aabcccccaaa"
        output = compress_string(s)
        self.assertEqual(output, "a2b1c5a3")


if __name__ == "__main__":
    unittest.main()
