class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_a = 0
        p1=0
        p2=len(heights)-1
        while p1<p2:
            a = (p2-p1)*(min(heights[p1],heights[p2]))
            best_a = max(a,best_a)
            if heights[p1] < heights[p2]:
                p1+=1
            elif heights[p1]>heights[p2]:
                p2-=1
            else:
                p1+=1
        return best_a


