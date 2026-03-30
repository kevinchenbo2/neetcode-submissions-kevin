class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = 0
        cache = [0] * m
        cache[m - 1] = 1
        
        for _ in range(n):
            for i in range(m - 1, -1, -1):
                if i != m - 1:
                    cache[i] += cache[i + 1]
        
        return cache[0]