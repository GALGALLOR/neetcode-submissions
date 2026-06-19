class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def get_value(item):
            return item[1]
        num_map = dict()
        for num in nums:
            num_map[num] = num_map.get(num,0)+1
        #sort from largest to k
        def return_val(item):
            return item[1]
        my_items = sorted(num_map.items(),key=return_val,reverse= True)
        my_new_list = []
        for item in my_items:
            my_new_list.append(item[0])
        return my_new_list[:k]