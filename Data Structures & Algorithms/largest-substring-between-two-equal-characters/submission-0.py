class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = defaultdict(int)
        max_len = -1

        for i in range(len(s)):
            if s[i] in seen:
                max_len = max(max_len, i - seen[s[i]] - 1)
                
            else:
                seen[s[i]] = i
        
        return max_len