class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMax, curMin = 1, 1
        for num in nums:
            temp = curMax * num
            curMax = max(num * curMin, num * curMax, num)
            curMin = min(num * curMin, temp, num)
            ans = max(ans, curMax)
        return ans



        