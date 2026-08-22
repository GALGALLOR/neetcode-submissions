class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        total = sum(nums)
        rightsum = total-leftsum

        for i,num in enumerate(nums):
            if num+leftsum == rightsum:
                return i
            leftsum +=num
            rightsum-=num
        return -1