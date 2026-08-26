class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rem_map = {}
        for i,num in enumerate(numbers):
            if target-num in rem_map:
                return [rem_map[target-num]+1,i+1]
            else:
                rem_map[num] = i
        return []