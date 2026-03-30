class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                t = stack.pop()
                ans[t] = i - t
            stack.append(i)
        
        while stack:
            i = stack.pop()
            ans[i] = 0
        return ans
                