class Solution:
    def isValid(self, s: str) -> bool:
        connection = {']': '[', '}' : '{', ')' : '('}
        
        stack = []
        for p in s:
            if p in connection:
                if stack and stack[-1] == connection[p]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(p)
        
        return False if stack else True
                
