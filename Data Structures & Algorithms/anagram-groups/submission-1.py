class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hash out the counts for each letter, and use them as keys
        #turn it into tuples
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        
        return list(ans.values())