class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def return_val(item):
            return item[1]
        mymap = {}
        for num in nums:
            mymap[num]=mymap.get(num,0)+1
        mymap_sorted = dict(sorted(mymap.items(),reverse=True,key=return_val))
        return list(mymap_sorted)[:k]