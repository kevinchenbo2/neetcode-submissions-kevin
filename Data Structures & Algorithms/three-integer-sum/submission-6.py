class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = 0
        nums.sort()
        while l < len(nums) - 2:
            #no more negatives so can't sum3 to 9
            if nums[l] > 0:
                break 
            # condition to check if the answer 
            # if cur element is same as previous
            # we do this to make sure we don't have dup answers
            # we already found all answers with the value at l
            if l > 0 and nums[l] == nums[l - 1]:
                l += 1
                continue
            
            #establish inner loop
            lo, hi = l + 1, len(nums) - 1
            while lo < hi:
                sum3 = nums[l] + nums[lo] + nums[hi]
                if sum3 > 0: hi -= 1
                elif sum3 < 0: lo += 1
                else:
                    ans.append([nums[l], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
            l += 1
        
        return ans
