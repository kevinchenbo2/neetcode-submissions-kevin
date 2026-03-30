class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] < temp:
                cold = stack.pop()
                ans[cold] = i - cold
            stack.append(i)
        return ans
                