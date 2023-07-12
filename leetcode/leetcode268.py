from typing import List

# https://leetcode.com/problems/missing-number/
class LeetCode268:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res
