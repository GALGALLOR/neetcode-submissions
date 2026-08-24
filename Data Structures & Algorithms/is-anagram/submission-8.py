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
            map_s[s[i]] = map_s.get(s[i],0)+1
            ##same for map_t
            map_t[t[i]] = map_t.get(t[i],0)+1
        #Compare keys in both maps 
        if map_s!=map_t:
            return False
        return True

        