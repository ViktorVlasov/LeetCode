"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
------------------------------------------------------------------------------------------------------------------
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
------------------------------------------------------------------------------------------------------------------
Example 2:
Input: nums = [0]
Output: [0]
------------------------------------------------------------------------------------------------------------------
Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""
#-------------------------------------------------------------------------------------------------
# *using an additional array*
# def moveZeroes(nums: list[int]) -> None:
#     res = [0] * len(nums)
#     res_pointer = 0
#     for nums_pointer in range(len(nums)):
#         if nums[nums_pointer] != 0:
#             res[res_pointer] = nums[nums_pointer]
#             res_pointer += 1
#     for i in range(len(nums)):
#         nums[i] = res[i]
#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------
# *slow solution*
# def moveZeroes(nums: list[int]) -> None:
#     r = len(nums) - 1
#     l = r - 1
#     while l >= 0:
#         if nums[l] == 0:
#             for i in range(l, r):
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#             r -= 1
#         l -= 1
#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------
# faster
# def moveZeroes(nums: list[int]) -> None:
#     try:
#         l = nums.index(0)
#         for r in range(l + 1, len(nums)):
#             if nums[r] != 0:
#                 nums[l] = nums[r]
#                 l += 1
#         for i in range(l, len(nums)):
#             nums[i] = 0
#     except ValueError as e:
#         pass
#-------------------------------------------------------------------------------------------------

#optimal
def moveZeroes(nums: list[int]) -> None:
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

#pytest
def test_1():
    nums = [0,1,0,3,12]
    output = [1,3,12,0,0]
    moveZeroes(nums)
    assert nums == output

def test_2():
    nums = [0]
    output = [0]
    moveZeroes(nums)
    assert nums == output