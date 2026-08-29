class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_a = 0
        p1=0
        p2=len(heights)-1
        while p1<p2:
            h = min(heights[p1],heights[p2])
            b = p2-p1
            a = b*h
            best_a = max(a,best_a)
            if heights[p1] < heights[p2]:
                p1+=1
            else:
                p2-=1
        return best_a


