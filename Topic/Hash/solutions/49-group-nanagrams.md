# solution1: hash
```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sort_s = tuple(sorted(s))
            if sort_s in dic:
                dic[sort_s].append(s)
            else:
                dic[sort_s] = [s]
        return dic.values()
        
```