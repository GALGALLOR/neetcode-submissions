class Solution:
    def firstUniqChar(self, s: str) -> int:
        si = -1
        mymap = {}
        for i,char in enumerate(s):
            if char in mymap:
                mymap[char].append(i)
            else:
                mymap[char] = [i]
        #print(mymap)
        for i in mymap:
            if len(mymap[i])==1:
                return mymap[i][0]
        return -1

            