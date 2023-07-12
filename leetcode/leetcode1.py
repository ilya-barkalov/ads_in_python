from typing import List


# https://leetcode.com/problems/two-sum/
class LeetCode1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BIGO time: 0(n)
        # BIGO memory: 0(n)
        hashset = {}
        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashset:
                return [hashset[diff], i]
            hashset[n] = i

        return []
