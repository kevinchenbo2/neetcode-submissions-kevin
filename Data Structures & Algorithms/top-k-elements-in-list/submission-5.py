class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1
        ans = []
        for i in range(k):
            num = max(seen, key=seen.get)
            ans.append(num)
            del seen[num]
        return ans
