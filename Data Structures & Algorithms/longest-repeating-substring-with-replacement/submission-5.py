class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        l = longest = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            longest = max(longest, seen[s[r]])

            if (r - l + 1) - longest > k:
                seen[s[l]] -= 1
                l += 1
        return r - l + 1