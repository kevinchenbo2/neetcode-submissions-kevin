class Solution:
    def isPalindrome(self, s: str) -> bool:
        r, l = len(s) - 1, 0
        while l < r:
            while not self.alphNum(s[r]) and l < r: r -= 1
            while not self.alphNum(s[l]) and r > l: l += 1
            if s[l].lower() != s[r].lower(): return False
            l, r = l + 1, r - 1
        return True

    def alphNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))