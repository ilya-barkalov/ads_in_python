from typing import List


# https://leetcode.com/problems/contains-duplicate/
class LeetCode217:
    def run(self, nums: List[int]) -> bool:
        # BIGO time: 0(n)
        # BIGO memory: 0(n)
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False
