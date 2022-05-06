"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
-----------------------------------------------------------------------------
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
-----------------------------------------------------------------------------
Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
-----------------------------------------------------------------------------
Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        res = [None] * len(nums)
        for index in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[index] = nums[left]**2
                left += 1
            else:
                res[index] = nums[right]**2
                right -= 1
        return res
       

# pytest
test = Solution()

def test_1():
    nums = [-4, -1, 0, 3, 10]
    output = [0, 1, 9, 16, 100]
    assert test.sortedSquares(nums) == output

def test_2():
    nums = [-7,-3,2,3,11]
    output = [4,9,9,49,121]
    assert test.sortedSquares(nums) == output