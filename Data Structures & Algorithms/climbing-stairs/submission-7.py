class Solution:
    def climbStairs(self, n: int) -> int:
        cur = 0
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        first = 1
        second = 2

        for i in range(2, n):
            cur = first + second
            first = second
            second = cur

        return cur
