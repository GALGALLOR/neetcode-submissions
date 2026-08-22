class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        right = 1
        left = 1
        for i in range(n):
            #Find products from left to right
            output[i] = left
            left *= nums[i]
        for i in range(n-1,-1,-1):
            output[i] *= right
            right *= nums[i]
        
        return output
