
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<1:
            return True
        mystack = []
        close_mapper = {'(':')','{':'}','[':']'}

        for i in range(len(s)):
            if s[i] in close_mapper:
                mystack.append(s[i])
            else:
                #if the prev stack[-1]'s mapped closure is s[i] pop
                if len(mystack)<=0:
                    return False
                curr = s[i]
                last_stack = mystack[-1]
                stack_invert = close_mapper[last_stack]
                if stack_invert == curr:
                    mystack.pop()
                else:
                    return False
        print(mystack)
        return not bool(mystack)
        