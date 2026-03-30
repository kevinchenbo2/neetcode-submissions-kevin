class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        window, t_count = defaultdict(int), defaultdict(int)
        for i in t:
            t_count[i] += 1
        
        have, l = 0, 0
        min_length = float("infinity")
        ans = [-1, -1]
        for r in range(len(s)):
            window[s[r]] += 1
            
            if s[r] in t_count and window[s[r]] == t_count[s[r]]:
                have += 1
                
            while have == len(t_count):
                if (r - l + 1) < min_length:
                    min_length = r - l + 1
                    ans = [l, r]
                    
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
                    
        l, r = ans
        return s[l : r + 1] if min_length != float("infinity") else ""
        