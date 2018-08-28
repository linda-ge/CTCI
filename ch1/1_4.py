import unittest
"""
1.4 palindrome permutation:
Given a string, write a function to check if it is a permutation of a palindrome.
"""


def palindrome_permutation(my_string):
    all_chars = {}
    my_string = my_string.lower()
    for char in my_string:
        if char == " ":
            pass
        elif not char in all_chars:
            all_chars[char] = 1
        else:
            all_chars[char] += 1

    odd_count = 0
    print(all_chars)
    for key in all_chars.keys():
        if all_chars[key] % 2 == 1:
            odd_count += 1
    if odd_count > 1:
        return False
    return True

class test_palindrome_permutation(unittest.TestCase):
    def test_true(self):
        self.assertTrue(palindrome_permutation("Tact Coa"))

    def test_false(self):
        self.assertFalse(palindrome_permutation("Linda"))


if __name__ == '__main__':
    unittest.main()
