class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        frq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            count[i] += 1
        for num in count:
            frq[count[num]].append(num)
        
        ans = []
        for i in range(len(frq) - 1, 0, -1):
            if frq[i]:
                for j in frq[i]:
                    ans.append(j)
                    if len(ans) == k:
                        return ans