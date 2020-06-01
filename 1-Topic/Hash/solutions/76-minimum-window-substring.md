# takeaway
这题其实更像slding-window，hash/set用来方便统计追踪的。  
# motivation
总的来说，这里的hash还是扮演一个计数板的角色，用来跟踪查重
```py
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # dict 的默认值问题记得弄清楚！
        d = {}
        for c in t:
            if c not in d: d[c] = 1
            else: d[c] += 1
        
        remain = len(t)
        start,end = 0,0
        res = ""
        while end < len(s):
            # extend end till meet standard
            while remain > 0 and end < len(s):
                if s[end] in d:
                    d[s[end]] -= 1
                    if d[s[end]] >= 0: remain -= 1
                end += 1 
            
            if remain == 0 and (res == "" or end - start < len(res)):
                res = s[start:end]
                
            # reset start pointer 
            while remain == 0 and start < end:
                if s[start] in d:
                    d[s[start]] += 1
                    if d[s[start]] > 0: 
                        remain += 1
                        
                start += 1
                if remain == 0 and (res == "" or end - start < len(res)):
                    res = s[start:end]
        return res
```