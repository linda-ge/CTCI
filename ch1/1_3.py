import unittest

"""
1.3 URLify a string by replacing " " with %20
"""

def urlify(string, length):
    i = 0
    urlstring = ""
    while i < length:
        if string[i] = " ":
            urlstring += "%20"
        else:
            urlstring += string[i]
        i += 1
    return urlstring


class test_urlify(unittest.TestCase):
    def test_simple(self):
        self.assertEqual()

    def test_next(self):
        self.assertNotEqual()

if __name__ == "__main__":
    unittest.main()
