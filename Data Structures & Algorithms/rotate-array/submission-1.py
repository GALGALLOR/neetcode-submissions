class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        sect1 = nums[:-k]
        sect2 = nums[-k:]

        newsect = sect2+sect1
        for i in range(len(nums)):
            nums[i] = newsect[i]

        
        