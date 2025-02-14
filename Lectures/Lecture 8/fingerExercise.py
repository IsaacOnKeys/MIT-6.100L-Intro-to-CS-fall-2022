"""Finger Exercise Lecture 8
Implement the function that meets the specifications below:"""

def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice 
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    # Your code here
    same = set(s1) == set(s2)
    return same


# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False

"""
Lame MIT Solution:
def same_chars(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    for i in s2:
        if i not in s1:
            return False
    return True

"""