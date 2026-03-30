class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        while left < right:
            while not s[right].isalnum() and right > 0: right -= 1
            while not s[left].isalnum() and left < len(s) - 1: left += 1
            if s[left].lower() != s[right].lower() and left < right: return False
            left += 1
            right -= 1
        return True