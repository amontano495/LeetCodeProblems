class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval(f,a,b):
            if f == '+':
                return a + b
            elif f == '-':
                return a -b
            elif f == '*':
                return a*b
            elif f == '/':
                return int(a / b)
        stack = []
        i = 0
        operators = ['+','-','*','/']
        
        if len(tokens) == 1:
            return tokens[0]
        
        while(i < len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
                i+=1
                
            if tokens[i] in operators:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(eval(tokens[i],int(op2),int(op1)))
                i+=1
        
        return stack.pop()