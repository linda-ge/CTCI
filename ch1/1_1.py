import unittest

def is_unique(check_string):
    """
    is_unique checks whether a string has all unique characters.
    if so, return true.
    else, return false.
    o(N) space and O(1) time, where N is the length of the string being checked.
    """
    new_set = set(check_string)
    return len(new_set) == len(check_string)

# no additional data structures:
"""
if you can't make new data structures, then it comes down to whether you
can sort in place. If you can, then I would sort in place for O(NlogN) time.
Then I would start from string[0] and compare it to the following index.
If the values are the same, return false.
Otherwise, I would reassign the current index to string[1] and compare to its
following index. Repeat. The worst case scenario is O(N), with N-1 compares.
Return True at the last index.
If I can't sort in place, compare the value at each index to all values after it.
Return false if a match is found. This is O(N^2) time.
"""



# TESTS

class test_string_methods(unittest.TestCase):
    def test_unique(self):
        self.assertTrue(is_unique("abcdefg"))
    def test_dup(self):
        self.assertFalse(is_unique("catatata"))
    def test_edge(self):
        self.assertTrue(is_unique(""))

if __name__ == "__main__":
    unittest.main()
