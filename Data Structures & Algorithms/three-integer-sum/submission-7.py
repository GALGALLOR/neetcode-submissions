class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for p1 in range(len(nums)):
            p2 = p1+1
            p3 = len(nums)-1
            while p2<p3:
                curr = nums[p1]+nums[p2]+nums[p3]
                if curr < 0:
                    p2+=1
                elif curr>0:
                    p3-=1
                else:
                    if [nums[p1],nums[p2],nums[p3]] in result:
                        pass
                    else:
                        result.append([nums[p1],nums[p2],nums[p3]])                    
                    p2+=1
                    p3-=1
        return result
