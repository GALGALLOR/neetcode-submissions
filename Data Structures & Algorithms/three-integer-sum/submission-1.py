class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        new_nums = sorted(nums)
        result=[]
        for p1 in range(len(new_nums)):
            p2=p1+1
            p3 = len(new_nums)-1
            while p2<p3:
                #print(f"p1: {p1}, p2: {p2}, p3: {p3}")
                if new_nums[p1]+new_nums[p2]+new_nums[p3]<0:
                    p2+=1
                elif new_nums[p2]+new_nums[p3]+new_nums[p1]>0:
                    p3-=1
                else:
                    if [new_nums[p1],new_nums[p2],new_nums[p3]] in result:
                        pass
                    else:
                        result.append([new_nums[p1],new_nums[p2],new_nums[p3]])
                    p2+=1
        #Remove duplicate
        return result
