class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        
        for height in heights:
            temp = [height, 1]
            while stack and stack[-1][0] >= height:
                temp[1] += stack.pop()[1]
            if stack:
                hMin = min(stack[-1][0], temp[0])
                max_area = max(max_area, hMin * (stack[-1][1] + temp[1]))
            max_area = max(max_area, temp[0] * temp[1])
            stack.append(temp)
        
        count = 0
        while stack:
            stack[-1][1] += count
            temp, count = stack.pop()
            max_area = max(max_area, temp * count)

        return max_area


