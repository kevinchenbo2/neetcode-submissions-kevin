class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]
        ans = 0
        while l < r:
            if max_left < max_right:
                l += 1 
                max_left = max(max_left, height[l])
                left = min(max_left, max_right) - height[l]
                if left > 0:
                    ans += left
            else:
                r -= 1
                max_right = max(max_right, height[r])
                right = min(max_left, max_right) - height[r]
                if right > 0:
                    ans += right
        return ans


        
            