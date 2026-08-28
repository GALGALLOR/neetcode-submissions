class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for i,num in enumerate(nums):
            if target-num in mymap:
                return [mymap[target-num],i]
            else:
                mymap[num] = i
        return []
            