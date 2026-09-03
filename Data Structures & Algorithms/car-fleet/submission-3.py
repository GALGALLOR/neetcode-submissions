class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #find remaining Time for each car
        p_t = [(position[i],(target-position[i])/speed[i]) for i in range(len(position))]
        p_t.sort(reverse=True)
        stack = []
        for p,t in p_t:
            if stack:
                if t>stack[-1]:
                    stack.append(t)
            else:
                stack.append(t)
        
        
        return len(stack)
        