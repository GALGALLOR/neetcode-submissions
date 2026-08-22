class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        R_i = {}
        for i,num in enumerate(nums):
            if num in R_i:
                return [R_i[num],i]
            R_i[target-num] = i
        return []