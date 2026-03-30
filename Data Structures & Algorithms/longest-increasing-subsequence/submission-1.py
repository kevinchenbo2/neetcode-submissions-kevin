class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        max_len = 0
        
        for i in range(len(nums) - 1, -1, -1):
            cur_len = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cur_len = max(cur_len, cache[j])
            cache[i] = cur_len + 1
            max_len = max(cur_len, max_len)
        
        return max_len