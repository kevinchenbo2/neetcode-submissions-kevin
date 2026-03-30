class Solution:
    def isValid(self, s: str) -> bool:
        connection = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in connection:
                if not stack or stack.pop() != connection[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack
        
        
                
