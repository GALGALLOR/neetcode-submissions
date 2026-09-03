class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums)-1
        

        while start<=stop:
            mid = start+int((stop-start)/2)
            #print(f"start:: {start},mid: {mid}, stop: {stop}")
            if nums[mid]>target:
                stop = mid-1
            elif nums[mid]<target:
                start = mid+1
            elif nums[mid]==target:
                return mid
            else:
                return -1
        return -1
                
        
        