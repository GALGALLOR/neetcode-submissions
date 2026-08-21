class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_list = Counter(nums)
        print(new_list.most_common(k))
        return [value[0] for value in new_list.most_common(k)]