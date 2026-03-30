class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                temp = stack.pop()
                max_area = max(max_area, temp[0] * (i - temp[1]))
                start = temp[1]
            stack.append([height, start])

        while stack:
            height, start = stack.pop()
            max_area = max(max_area, height * (len(heights) - start))

        return max_area


