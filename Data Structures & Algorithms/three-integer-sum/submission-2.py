class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        new_nums = nums.sort()
        result=[]
        for p1 in range(len(nums)):
            p2=p1+1
            p3 = len(nums)-1
            while p2<p3:
                #print(f"p1: {p1}, p2: {p2}, p3: {p3}")
                if nums[p1]+nums[p2]+nums[p3]<0:
                    p2+=1
                elif nums[p2]+nums[p3]+nums[p1]>0:
                    p3-=1
                else:
                    if [nums[p1],nums[p2],nums[p3]] in result:
                        pass
                    else:
                        result.append([nums[p1],nums[p2],nums[p3]])
                    p2+=1
        #Remove duplicate
        return result
