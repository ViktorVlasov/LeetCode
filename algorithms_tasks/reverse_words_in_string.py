"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

def reverseWords(s: str) -> str:
    return ' '.join([i[::-1] for i in s.split(' ')])



def test_1():
    s = "Let's take LeetCode contest"
    output = "s'teL ekat edoCteeL tsetnoc"
    assert reverseWords(s) == output

def test_2():
    s = "God Ding"
    output = "doG gniD"
    assert reverseWords(s) == output

def test_3():
    s = "ab"
    output = "ba"
    assert reverseWords(s) == output