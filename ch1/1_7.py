import unittest
"""
1.7 rotate matrix:

"""



class test_rotate_matrix(unittest.TestCase):
    def test_true(self):
        self.assertTrue()

    def test_false(self):
        self.assertFalse()


if __name__ == '__main__':
    unittest.main()

"""unique morse words draft
any way to not use += which duplicates the string at every step?
takes a list of words and returns the number of unique representations in morse code
space = O(w) where w is the number of unique morse representations -- set
time = O(char*word) or the total number of characters in words (the list of words)
consider possible time optimizations when looking at the other solutions

do i need a dictionary?

STUDY THE INVERSE, WHICH REQUIRES DYNAMIC PROGRAMMING -- SEE DENERO LECTURE ON MEMOIZATION
"""
def unique_morse_words(words):
    morse = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    morse_set = set()
    for word in words:
        newstr = ''
        for char in word:
            newstr += morse[letters.find(char)]
        morse_set.add(newstr) #are you sure that it is add? look at documentation
    return len(morse_set)
