class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_neg = -1
        inc = []
        inc.append(nums[0])
        if nums[0] < 0:
            first_neg = 0
        max_area = inc[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if inc[i - 1] == 0:
                inc.append(num)
                if num < 0:
                    first_neg = i
                else: first_neg = -1
                max_area = max(inc[i], max_area)
            else:
                inc.append(inc[i-1] * num)
                if inc[i] < 0:
                    if first_neg == -1:
                        first_neg = i
                    max_area = max(max_area, inc[i]/inc[first_neg])
                else:
                    max_area = max(max_area, inc[i])
        
        return int(max_area)


        