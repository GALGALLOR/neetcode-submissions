class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        stack = [intervals[0]]
        for curr in intervals:
            #compare curr to last thing in stack
            #if curr is better than last
            #if curr is inside last
            #if curr is less than last
            if curr[0]>stack[-1][1]:
                stack.append(curr)
            else:
                stack[-1][1] = max(stack[-1][1],curr[1])
        return stack
            

