class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) / 2
        sums = {0}
        for num in nums:
            if (target - num) in sums:
                return True
            for n in list(sums):
                sums.add(n + num)
        
        return False
            