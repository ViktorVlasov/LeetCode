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

def test_simple_array():
    test = Solution()
    nums = [-1,0,3,5,9,12] 
    target = 9
    assert test.search(nums, target) == 4

def test_otherwise():
    test = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    assert test.search(nums, target) == -1

def test_corner_left():
    test = Solution()
    nums = [-1,0,3,5,9,12]
    target = -10
    assert test.search(nums, target) == -1

def test_corner_right():
    test = Solution()
    nums = [-1,0,3,5,9,12]
    target = 13
    assert test.search(nums, target) == -1