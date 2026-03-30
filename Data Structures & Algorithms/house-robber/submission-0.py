class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        prev_rob = nums[0]
        prev_skip = 0

        for i in range(1, len(nums)):
            current_rob = nums[i] + prev_skip

            current_skip = max(prev_rob, prev_skip)

            prev_rob, prev_skip = current_rob, current_skip

        return max(prev_rob, prev_skip)