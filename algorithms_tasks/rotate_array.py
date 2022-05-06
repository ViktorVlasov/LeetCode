"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
------------------------------------------------------------------
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
------------------------------------------------------------------
Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
------------------------------------------------------------------
Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
"""

# first way to solve (slow), dont pass test_5()
# def rotate(nums: list[int], k: int) -> None:
#     for _ in range(k):
#         for i in range(len(nums) - 1, 0, -1):
#             nums[i], nums[i - 1] = nums[i - 1], nums[i]

def rotate(nums: list[int], k: int) -> None:
    if k > len(nums):
        k = k % len(nums)
    new_nums = nums[len(nums) - k:len(nums)] + nums[0:len(nums) - k]
    for i in range(len(new_nums)):
        nums[i] = new_nums[i]

#pytest
import random

def test_1():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    output = [5, 6, 7, 1, 2, 3, 4]
    rotate(nums, k)
    assert nums == output

def test_2():
    nums = [-1, -100, 3, 99]
    k = 2
    output = [3, 99, -1, -100]
    rotate(nums, k)
    assert nums == output

def test_3():
    nums = [1]
    k = 10
    output = [1]
    rotate(nums, k)
    assert nums == output

def test_4():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 99554
    output = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, k)
    assert nums == output

def test_5():
    nums = [random.randint(-2**31, 2**31 - 1) for i in range(10**5)]
    k = 10**5
    output = list(nums)
    rotate(nums, k)
    assert nums == output

def test_6():
    nums = [1,2]
    k = 5
    output = [2,1]
    rotate(nums, k)
    assert nums == output