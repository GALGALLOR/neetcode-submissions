class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #make them into a hashmap eg Char: count
        s_map = dict()
        t_map = dict()
        for char in s:
            s_map[char] = s_map.get(char,0)+1
        for char in t:
            t_map[char] = t_map.get(char,0)+1
        if len(s_map) != len(t_map):
            return False
        for item in s_map:
            #compare key counts
            if item in t_map:
                if s_map[item] != t_map[item]:
                    return False
            else:
                return False
        return True
        