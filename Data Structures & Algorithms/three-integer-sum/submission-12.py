class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        j = len(nums)-1
        res = []
        if not nums:
            return [[]]
        for i in range(0,len(nums)-1):
            if i>0:
                if nums[i]==nums[i-1]:
                    continue
            m = i+1
            j = len(nums)-1
            while m<j:
                if nums[i]+nums[m]+nums[j] == 0:
                    res.append([nums[i],nums[m],nums[j]])
                    m+=1
                    j-=1
                    while m<j and nums[j]==nums[j+1]:
                        j-=1
                    while m>i and nums[i]==nums[i-1]:
                        i+=1
                elif nums[i]+nums[m]+nums[j]<0:
                    m+=1
                    continue
                elif nums[i]+nums[m]+nums[j]>0:
                    j-=1
                    continue
            
        return res
                    


        
