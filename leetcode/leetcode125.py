# https://leetcode.com/problems/valid-palindrome/
class LeetCode125:
    def isPalindrome(self, s: str) -> bool:
        # BIGO time: O(n)
        # BIGO memory: O(1)

        left = 0
        right = len(s) - 1

        while left < right:
            left_char = s[left]
            right_char = s[right]

            if not left_char.isalnum():
                left += 1
                continue

            if not right_char.isalnum():
                right -= 1
                continue

            if left_char.lower() != right_char.lower():
                return False

            left += 1
            right -= 1

        return True
