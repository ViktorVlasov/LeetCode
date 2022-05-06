class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = -1
        r = len(nums)
        while l < r - 1:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        if r < len(nums) and target == nums[r]:
            return r
        return -1

# pytest
nums = [-1, 0, 3, 5, 9, 12] 
test = Solution()

def test_simple_array():
    target = 9
    assert test.search(nums, target) == 4

def test_otherwise():
    target = 2
    assert test.search(nums, target) == -1

def test_corner_left():
    target = -10
    assert test.search(nums, target) == -1

def test_corner_right():
    target = 13
    assert test.search(nums, target) == -1