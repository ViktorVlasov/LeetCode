"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
---------------------------------------
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
---------------------------------------
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

def searchInsert(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1 
    return l


# pytest
nums = [1, 3, 5, 6]

def test_1():
    target = 5
    assert searchInsert(nums, target) == 2

def test_2():
    target = 2
    assert searchInsert(nums, target) == 1

def test_3():
    target = 7
    assert searchInsert(nums, target) == 4

def test_4():
    target = -1
    assert searchInsert(nums, target) == 0