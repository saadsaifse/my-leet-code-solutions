'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #uniqueStrs = list(set(strs)) #remove duplicates
        output = []
        hashMap = dict()
        index = 0
        for i, s in enumerate(strs):
            s_sorted = ''.join(sorted(s))
            if s_sorted in hashMap:
                j = hashMap[s_sorted]
                output[j].append(s)
            else:
                hashMap[s_sorted] = index
                index += 1
                output.append([s])    
        return output
'''    

# Elena's solution below is much slower

import itertools
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_tuples = [("".join(sorted(list(a))), a) for a in strs] 
        sorted_tuples.sort(key = lambda x: x[0])
        grouped_list =  [list(group) for key, group in itertools.groupby(sorted_tuples, lambda x: x[0])]
        res = [[c for (a, c) in b] for b in grouped_list]
        return res
    
if __name__ == "__main__":
    s = Solution()
    output = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(output)