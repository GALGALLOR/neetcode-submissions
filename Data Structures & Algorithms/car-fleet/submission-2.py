class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #find remaining Time for each car
        p_t = [(position[i],(target-position[i])/speed[i]) for i in range(len(position))]
        p_t.sort()
        stack = []
        for i in reversed(range(0,len(p_t))):
            if stack:
                if p_t[i][1]>p_t[stack[-1]][1]:
                    stack.append(i)
            else:
                stack.append(i)
        
        
        return len(stack)
        