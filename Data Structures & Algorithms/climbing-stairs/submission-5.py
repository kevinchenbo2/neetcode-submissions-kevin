seen = defaultdict(int)
class Solution:
    
    def climbStairs(self, n: int) -> int:
        ans, two = 1, 1
        for _ in range(n - 1):
            temp = ans
            ans += two
            two = temp
        
        return ans