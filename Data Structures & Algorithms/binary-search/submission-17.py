class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        mid = int(len(nums)/2)
        stop = len(nums)
        
        while True:
            print(nums[start:stop],f"start: {start}, mid: {mid}, stop: {stop}")
            if len(nums[start:stop])<1:
                return -1
            elif len(nums[start:stop])==1:
                if nums[mid]==target:
                    return mid
                else:
                    return -1
            elif len(nums[start:stop])==2:
                if nums[start]==target:
                    return start
                elif nums[mid]==target:
                    return mid
                else:
                    return -1
            else:
                #check at mid
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    stop = mid
                    mid = start+int((stop-start)/2)
                elif nums[mid]<target:
                    start = mid
                    mid = start+int((stop-start)/2)
                else:
                    return -1

            
        return -1