
class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        for char in s:
            if char=='(' or char=='{' or char=='[':
                mystack.append(char)
                continue
            if len(mystack)<1:
                return False
            if char==')' and mystack[-1]=='(':
                mystack.pop()
            elif char=='}' and mystack[-1]=='{':
                mystack.pop()
            elif char==']' and mystack[-1] == '[':
                mystack.pop()
            else:
                return False
        if mystack:
            return False
        else:
            return True
        