class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums: counts[i] += 1
        freq = [[] for i in range(len(nums) + 1)]
        for i, n in counts.items():
            freq[n].append(i)
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k: return ans
