class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_dict = {}
        for item in strs:
            item_2 = ''.join(sorted(item)) #act, cat == act,act
            if item_2 in master_dict:
                master_dict[item_2].append(item)
            else:
                master_dict[item_2] = [item]
        return list(master_dict.values())
