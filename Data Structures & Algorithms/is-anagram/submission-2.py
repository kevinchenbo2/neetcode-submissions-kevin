class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict(int)
        if len(s) != len(t): return False
        for i in s:
            chars[i] += 1
        for i in t:
            if chars[i] == 0: return False
            chars[i] -= 1
        return True