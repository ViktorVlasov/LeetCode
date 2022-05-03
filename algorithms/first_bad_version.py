"""You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and 
you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Input: n = 5, bad = 4
Output: 4

Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 2^31 - 1
"""


class Solution:
    # for tests
    def __init__(self, bad: int) -> None:
        self.bad = bad

    def isBadVersion(self, version: int) -> bool:
        return version >= self.bad

    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r - 1:
            m = (l + r) // 2
            if self.isBadVersion(m):
                r = m
            else:
                l = m
        if self.isBadVersion(l):
            return l
        return r


# pytest       
def test_simple():
    n = 5
    bad = 4
    test = Solution(bad)
    assert test.firstBadVersion(n) == bad

def test_corner_left():
    n = 5
    bad = 1
    test = Solution(bad)
    assert test.firstBadVersion(n) == bad

def test_corner_right():
    n = 5
    bad = 5
    test = Solution(bad)
    assert test.firstBadVersion(n) == bad

def test_one_size():
    n = 1
    bad = 1
    test = Solution(bad)
    assert test.firstBadVersion(n) == bad