import unittest
"""
1.5 one away:
3 operations: insert, remove, replace.
given two strings, write a function to check if they are <= one edit away.
"""


def one_away(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    elif len(a) == len(b):
        return one_replace(a,b)
    elif len(a) - len(b) == -1:
        return insert_remove(b, a)
    else:
        return insert_remove(a,b)

def one_replace(a,b):
    """
    up to 1 edit but could be the same string
    """
    diff = 0
    i = 0
    while i < len(a):
        if a[i] != b[i]:
            diff += 1
        i += 1
    return diff <= 1

def insert_remove(larger, smaller):
    """
    up to 1 insert/remove. could not be the same string as lengths are different.
    """
    diff = 0
    i = 0
    j = 0
    while i < len(larger) and j < len(smaller):
        if larger[i] == smaller[j]:
            i += 1
            j += 1
        elif larger[i] != smaller[j]:
            diff += 1
            i += 1
    return diff == 1

class test_one_away(unittest.TestCase):
    def test_true(self):
        self.assertTrue(one_away("pale","ple"))

    def test_true_equal(self):
        self.assertTrue(one_away("trek","trek"))

    def test_false(self):
        self.assertFalse(one_away("turk","trek"))

    def test_false_length(self):
        self.assertFalse(one_away("trust","tru"))


if __name__ == '__main__':
    unittest.main()
