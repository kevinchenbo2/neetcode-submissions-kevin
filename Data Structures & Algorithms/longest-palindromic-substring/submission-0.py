class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_count = 0
        substring = ""
        for i in range(len(s)):
            odd = self.countPalindrome(s, i, i)
            even = self.countPalindrome(s, i, i + 1)
            if odd > max_count:
                max_count = odd
                half = odd // 2
                substring = s[i - half:i + half + 1]
            if even > max_count:
                max_count = even
                half = even // 2
                substring = s[i - half + 1:i + half + 1]
        
        return substring
    
    def countPalindrome(self, s, l, r) -> int:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1