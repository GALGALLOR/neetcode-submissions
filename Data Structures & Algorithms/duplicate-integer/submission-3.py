class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for item in nums:
            hashmap[item] = hashmap.get(item,0) + 1
            if hashmap[item] > 1:
                return True
        return False

        