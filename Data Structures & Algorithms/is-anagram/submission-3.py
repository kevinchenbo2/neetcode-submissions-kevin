class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        chars = defaultdict(int)
        for i in s:
            chars[i] += 1
        for i in t:
            if chars[i] == 0: return False
            chars[i] -= 1
        return True