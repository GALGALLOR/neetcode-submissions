class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total_stack = []
        operations = "+-*/"
        for i in range(len(tokens)):
            #add stuff to stack and if we come across an operand, we pop off 2 and perform calculation
            if tokens[i] in operations:
                val2 = total_stack.pop()
                val1 = total_stack.pop()
                if tokens[i]=='+':
                    ans = val1+val2
                elif tokens[i]=='-':
                    ans = val1-val2
                elif tokens[i]=='*':
                    ans = val1*val2
                else:
                    ans = math.trunc(val1/val2)
                #add it back to stack
                total_stack.append(ans)
            else:
                total_stack.append(int(tokens[i]))

        return total_stack[-1]