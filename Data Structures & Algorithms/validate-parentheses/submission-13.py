
class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        adds = '([{'
        for i in range(len(s)):
            if s[i] in adds:
                mystack.append(s[i])
            else:
                if len(mystack)<=0:
                    return False
                else:
                    if s[i]=='}' and mystack[-1]=='{':
                        mystack.pop()
                    elif s[i]==']' and mystack[-1]=='[':
                        mystack.pop()
                    elif s[i]==')' and mystack[-1]=='(':
                        mystack.pop()
                    else:
                        return False
        return len(mystack)==0
        