class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        max_len = 0
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cache[i] = max(cache[i], 1 +cache[j])
            max_len = max(cache[i], max_len)
        
        return max_len