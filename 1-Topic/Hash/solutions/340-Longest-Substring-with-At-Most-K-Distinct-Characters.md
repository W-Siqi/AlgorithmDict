# slding window + hash
这是hash还是扮演一个类似于counter的角色。  
**其实，只要是找对出现次数,冲突 有要求的子集/substring，基本都是要用到**
```py
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k < 1: return 0
        
        start,end,res = 0,0,0
        count = {}
        while end < len(s):
            while end < len(s):
                if s[end] in count:
                    count[s[end]] += 1
                elif len(count) < k:
                    count[s[end]] = 1
                else:
                    break
                end += 1
                
            res = max(res,end - start)
            
            while start < end:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                    start += 1
                    break
                start += 1
        return res
```