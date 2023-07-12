from typing import List


# https://leetcode.com/problems/single-number/
class LeetCode136:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
