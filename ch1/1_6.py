import unittest
"""
1.6 string compression:
basic string compression w/ counts of repeated chars.
e.g. aabcccccaaa would become a2b1c5a3. if the compressed string is not smaller
than original string, return the original string. Assume only uppercase and lowercase letters.

Assuming case-sensitive.

helper method?
newstr

curr_count = 1
if word[curr] == word[prev]
    curr_count += 1
if word[curr] != word[prev]
    word[prev] + curr_count (e.g. a2)
    curr_count = 1
prev = curr
curr += 1

pass off to stringbuilder function******

"""
#initial try cuts off the last character set a3
def string_compress(word):
    #ab; aa
    if len(word) <= 2:
        return word
    new_word = ''
    curr, prev = 1, 0
    curr_count = 1
    while curr + 1 < len(word) and len(new_word) < len(word):
        if word[curr] == word[prev]:
            curr_count += 1
        elif word[curr] != word[prev]:
            new_word += word[prev] + str(curr_count)
            curr_count = 1
        prev = curr
        curr += 1
    if len(new_word) < len(word):
        return new_word
    return word

#second try
def compress_count(word):
    if len(word) <= 2:
        return word
    new_word = ''
    curr_count = 0
    curr = 0
    while len(new_word) < len(word):
        if word





class test_string_compress(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(string_compress('aabcccccaaa'),'a2b1c5a3')

if __name__ == '__main__':
    unittest.main()
