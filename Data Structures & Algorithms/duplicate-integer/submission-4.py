class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set(nums)
        print(myset)
        return not (len(myset) == len(nums))

        