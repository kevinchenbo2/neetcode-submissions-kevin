class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0
        while l < r:
            while not s[r].isalnum() and l < r: r -= 1
            while not s[l].isalnum() and r > l: l += 1
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True