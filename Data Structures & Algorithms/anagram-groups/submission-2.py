class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                i = ord(c) - ord('a')
                count[i] += 1
            counts[tuple(count)].append(word)
        
        ans = []
        for group in counts:
            ans.append(counts[group])
        
        return ans
            