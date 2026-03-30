class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for car in pairs:
            time = (target - car[0])/car[1]
            if stack and stack[-1] < time:
                stack.append(time)
            elif not stack: 
                stack.append(time)
            
        
        return len(stack)