from typing import List


# https://leetcode.com/problems/move-zeroes/
class LeetCode283:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        # left, right, bound = 0, 0, len(nums) - 1
        # while left < bound:
        #     if left == right and right < bound:
        #         right += 1
        #
        #     if nums[left] == 0 and nums[right] != 0:
        #         nums[left], nums[right] = nums[right], 0
        #     elif nums[left] == 0 and nums[right] == 0 and right < bound:
        #         right += 1
        #         continue
        #
        #     left += 1
