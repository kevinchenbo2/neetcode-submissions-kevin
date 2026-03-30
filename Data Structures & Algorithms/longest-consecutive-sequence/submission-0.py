class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        longest = 0
        for i in nums:
            if i not in seen:
                if i - 1 in seen and i + 1 in seen:
                    length = seen[i - 1] + 1 + seen[i + 1]
                    seen[i - seen[i - 1]] = length
                    seen[i + seen[i + 1]] = length
                    seen[i] = 1
                    longest = max(longest, length)
                elif i - 1 in seen:
                    length = seen[i - 1] + 1
                    seen[i - seen[i - 1]] = length
                    seen[i] = length
                    longest = max(longest, length)
                elif i + 1 in seen:
                    length = seen[i + 1] + 1
                    seen[i + seen[i + 1]] = length
                    seen[i] = length
                    longest = max(longest, length)
                else: 
                    seen[i] = 1
                    longest = max(1, longest)
            
        return longest