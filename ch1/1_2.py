import unittest

"""
1.2 is one string a permutation of the other?
"""

def is_permutation(a,b):
    if len(a) != len(b):
        return False
    instances = {}
    for char in a:
        if not char in instances:
            instances[char] = 1
        else:
            instances[char] += 1
    for char in b:
        if not char in instances:
            instances[char] = 1
        else:
            instances[char] -= 1
    if sum(instances.values()) != 0:
        return False
    return True

# TESTS

class test_permutation(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_permutation("hahah", "hhhaa"))

    def test_false(self):
        self.assertFalse(is_permutation("hello", "world"))

    def test_length(self):
        self.assertFalse(is_permutation("hi", "there"))

if __name__ == '__main__':
    unittest.main()
