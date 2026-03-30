class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1
        while l < r: 
            maxWater = max(maxWater, (r - l) * min(heights[r], heights[l]))
            if heights[r] < heights[l]: r -= 1
            elif heights[l] <= heights[r]: l += 1
        
        return maxWater