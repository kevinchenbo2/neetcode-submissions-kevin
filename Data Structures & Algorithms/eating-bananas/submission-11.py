class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 - 25
        # 
        # does each one have a guaranteed answer
        # upper bound is max of all entries
        # 12, 13
        # we start with 4, obviously this works, let's go with 2: 2 * 4 slots = 8
        # Sort out the list first, you can work all the way down the list and do
        # a binary search at each time

        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            count = sum((p + mid - 1) // mid for p in piles)
            
            if count <= h:
                r = mid - 1
            else:
                l = mid + 1
                

        return l


        
