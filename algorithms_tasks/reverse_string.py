"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l = 0
    r = len(s) - 1
    while r > l:
        s[l], s[r] = s[r], s[l]
        r -= 1
        l += 1

    # or
    #s[:] = s[::-1]

def test_1():
    s = ["h","e","l","l","o"]
    output = ["o","l","l","e","h"]
    reverseString(s)
    assert s == output

def test_2():
    s = ["H","a","n","n","a","h"]
    output = ["h","a","n","n","a","H"]
    reverseString(s)
    assert s == output