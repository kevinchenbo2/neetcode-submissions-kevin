class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)
        for i in nums: dictionary[i] += 1
        counts = [[] for i in range(len(nums) + 1)]
        for n, c in dictionary.items():
            counts[c].append(n)
        ans = []
        for i in range(len(counts) - 1, 0, -1):
            for n in counts[i]:
                ans.append(n)
                if len(ans) == k: return ans
