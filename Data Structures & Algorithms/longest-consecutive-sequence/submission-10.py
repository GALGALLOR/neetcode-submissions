class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #debug
        for num in nums:
            if num%2==1:
                print(num)
        #Sort
        #Count order
        new_nums = sorted(set(nums))
        print(new_nums)
        count=1
        mini_count=1
        if len(new_nums)==1:
            return 1
        if len(new_nums)<1:
            return 0
        for i in range(1,len(new_nums)):
            print(f"count: {count}")
            print(f"mini_count: {mini_count}")
            print("----")
            print(f"num : {new_nums[i]}")
            if new_nums[i-1]+1==new_nums[i]:
                #if i==1:
                if mini_count==0:
                    mini_count+=1
                else:
                    mini_count+=1
                if mini_count>count:
                    count=mini_count
            else:
                if mini_count>count:
                    count=mini_count
                mini_count=1
        return count

