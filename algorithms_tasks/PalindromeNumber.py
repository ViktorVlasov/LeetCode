# https://leetcode.com/problems/palindrome-number/submissions/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x)[::-1] == str(x)

        if x < 0:
            return False
        new = 0
        orig = x
        while x:
            x, d = divmod(x, 10)
            new = new * 10 + d

        return orig == new