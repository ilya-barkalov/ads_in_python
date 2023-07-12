# https://leetcode.com/problems/find-the-difference/
class LeetCode389:
    def findTheDifference(self, s: str, t: str) -> str:
        # BIGO time: 0(n)
        # BIGO memory: 0(1)
        diff = 0
        for char in s:
            diff ^= ord(char)
        for char in t:
            diff ^= ord(char)
        return chr(diff)

        # BIGO time: 0(n)
        # BIGO memory: 0(n)
        # set1, set2 = {}, {}
        # for tmp in s:
        #     set1[tmp] = 1 + set1.get(tmp, 0)
        # for tmp in t:
        #     set2[tmp] = 1 + set2.get(tmp, 0)
        # for key in set2:
        #     if key not in set1:
        #         return key
        #     elif key in set1 and set1[key] != set2[key]:
        #         return key
        # return
