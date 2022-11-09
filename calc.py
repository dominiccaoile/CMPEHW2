import math

class Solution:
    def calculate(self, s):
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)           
            if op == "/": stack.append(float(stack.pop() / v))      
            if op == "%":stack.append(float(stack.pop())//v)
            if op == "^":stack.append(stack.pop()**v)
    
        it, num, stack, sign = 0, 0, [], "+"
        s = s.replace("**", "^")
        s = s.replace("//", "%")

        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/^%":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == "(":                                       
                num, j = self.calculate(s[it + 1:])
                it = it + j
            elif s[it] == ")":                                       
                update(sign, num)
                return sum(stack), it + 1
            it += 1
        update(sign, num)
        return sum(stack)

def calculator(calc):
    
    x = Solution()
    output = x.calculate(calc)
    print(output)


















    


