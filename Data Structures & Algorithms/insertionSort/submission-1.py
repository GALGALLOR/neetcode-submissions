# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        #Input: list of obj pairs
        #each obj is: k,value
        #create a list of pairs
        
        process = []
        new_pairs = self.pairs_to_list(pairs)
        #Now that we have created new_pairs
        if len(pairs)<1:
            return []
        process.append(new_pairs)
        
        for i in range(1,len(pairs)):
            current = pairs[i]
            j = i-1
            while j>=0 and pairs[j].key>current.key:
                pairs[j+1] = pairs[j]
                j = j-1
            pairs[j+1] = current
            process.append(self.pairs_to_list(pairs))

        return process
            

    def pairs_to_list(self,pairs):
        new_pairs=[]
        for item in pairs:
            new_pairs.append(item)
        return new_pairs