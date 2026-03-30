class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = defaultdict(int)
        for i in s:
            seen[i] += 1
        for i in t:
            if i not in seen or seen[i] == 0:
                return False
            seen[i] -= 1
        return True