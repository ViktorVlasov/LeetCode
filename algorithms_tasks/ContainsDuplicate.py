#https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums = sorted(nums)
        # uniq_nums = sorted((set(nums)))
        # return not (nums == uniq_nums)

        return len(nums) != len(set(nums))