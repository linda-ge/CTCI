"""
1.9 string_rotation
assume "erbottlewat" is s1 and s2 is "waterbottle"
assume first parameter in is_substring function signature is the substring to test against the second paramter
"""

def string_rotation(s1, s2):
    s1_2 = s1 + s1
    return is_substring(s2, s1_2)
