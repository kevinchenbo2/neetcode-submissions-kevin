class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for t in tokens:
            if t == "+":
                numbers.append(numbers.pop() + numbers.pop())
            elif t == "-":
                num1 = numbers.pop()
                num2 = numbers.pop()
                numbers.append(num2 - num1)
            elif t == "*":
                numbers.append(numbers.pop() * numbers.pop())
            elif t == "/":
                num1 = numbers.pop()
                num2 = numbers.pop()
                numbers.append(int(float(num2)/num1))
            else:
                numbers.append(int(t))
        
        return numbers[-1]
            