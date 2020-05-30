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