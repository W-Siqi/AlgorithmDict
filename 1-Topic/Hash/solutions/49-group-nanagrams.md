# PS: python 的ASCII和char的互转 asc = ord(char) c = chr(asc)

# solution1: 用 sort hash 
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

# solution2：用计数hash
这里的一个优化及时，不用abcd...都编码
a1b1c0d0...z0 的0都可省略。这依然保证hash值正确
```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def calKey(string):
            counts = [0]*26
            for char in string:
                counts[ord(char)-ord('a')] += 1
            res = ""
            for i,c in enumerate(counts):
                if c != 0: 
                    res += chr(i+ord('a'))
                    res += str(c)
            
            return res
        
        words = {}
        for s in strs:
            key = calKey(s)
            if key not in words:
                words[key] = [s]
            else:
                words[key].append(s)
        
        return words.values()
```