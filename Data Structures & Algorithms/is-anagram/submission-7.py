class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        #Declare HashMaps for both
        #{c:1,a:1,t:2}, {a:1,c:1,t:2}
        #{c:1,a:1,t:1}, {c:1,a:1,r:1}
        map_t = {}
        map_s = {}

        for i in range(len(s)):
            if s[i] in map_s:
                map_s[s[i]] += 1
            else:
                map_s[s[i]] = 1
            ##same for map_t
            if t[i] in map_t:
                map_t[t[i]] +=1
            else:
                map_t[t[i]] = 1
        #Compare keys in both maps 
        for key_s in map_s:
            if not (key_s in map_s and key_s in map_t):
                return False
            if map_s[key_s] != map_t[key_s]:
                return False
        return True

        