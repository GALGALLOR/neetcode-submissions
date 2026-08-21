class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_dict = {} #{art:[rat]}, final, final
        for word in strs:
            new_word = ''.join(sorted(word))
            if new_word in master_dict:
                master_dict[new_word].append(word)
            else:
                master_dict[new_word] = [word]
        return [word for word in master_dict.values()]