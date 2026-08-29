class Solution:
    def trap(self, height: List[int]) -> int:
        p1=0
        p2=len(height)-1
        maxl = 0
        maxr = 0
        total = 0
        while p1<p2:
            if height[p1]>height[p2]:
                if (maxr - height[p2])<0:
                    total+=0
                else:
                    total +=maxr - height[p2]
                maxr = max(maxr,height[p2])
                p2-=1
            else:
                if (maxl-height[p1])<0:
                    total+=0
                else:
                    total += maxl - height[p1]
                maxl = max(maxl,height[p1])
                p1 +=1
        return total
