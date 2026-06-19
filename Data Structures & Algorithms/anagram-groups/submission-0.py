class Solution:
    def sortString(self,string):
        x = ''.join(sorted(string))
        return x
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort each string
        new_strs = []
        st_map = dict()
        for st in strs:
            new_strs.append(self.sortString(st))
            # [cat,act,hat] -> [act,act,aht] -> {act:[cat,act],hat:[hat]}
            # strs              new_strs          st_map
            curr_list = st_map.get(self.sortString(st),[])
            curr_list.append(st)
            st_map[self.sortString(st)] = curr_list

        #convert dict to List
        return list(st_map.values())