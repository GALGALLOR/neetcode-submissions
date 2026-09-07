class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strings = ""
        fword = strs[0]
        for i,char in enumerate(fword):
            is_present = True
            for word in strs:
                if len(word)<i+1:
                    return strings
                if fword[i] == word[i]:
                    pass
                else:
                    is_present = False
                    return strings
            if is_present:
                strings+=char
        return strings


        