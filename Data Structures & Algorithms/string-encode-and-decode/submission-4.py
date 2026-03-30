class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "#" + i
        return encoded
    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": j += 1
            length = int(s[i:j])
            ans.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return ans
            
