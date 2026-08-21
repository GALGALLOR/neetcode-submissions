class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_targets = {}
        for idx,num in enumerate(nums):
            rem_target = target-num
            if rem_target in dict_targets:
                return [dict_targets[rem_target],idx]
            else:
                dict_targets[num] = idx
        return []
        
        
        '''for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []'''