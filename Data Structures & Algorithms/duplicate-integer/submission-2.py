class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Convert into a hashset
        nums_set = set(nums)

        #compare length
        if len(nums_set) == len(nums):
            return False
        else:
            return True

        