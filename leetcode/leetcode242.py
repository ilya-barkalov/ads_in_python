
# https://leetcode.com/problems/valid-anagram/
class LeetCode242:
    def isAnagram(self, s: str, t: str) -> bool:
        # BIGO time: 0(n)
        # BIGO memory: 0(n)
        if len(s) != len(t):
            return False

        dict_s, dict_t = {}, {}

        for index in range(len(s)):
            dict_s[s[index]] = 1 + dict_s.get(s[index], 0)
            dict_t[t[index]] = 1 + dict_t.get(t[index], 0)

        for dictKey in dict_s:
            if dictKey in dict_t and dict_s[dictKey] == dict_t[dictKey]:
                continue
            else:
                return False

        return True
