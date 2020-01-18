```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        res = ""
        for i in range(len(s)):
            ps = self.getPS(s,i)
            res = ps if len(ps)>len(res) else res
            
        return res
    
    def getPS(self, s, center):
        le = ri = center
        # expend 1
        while ri < len(s) and s[ri]==s[center]:
            ri += 1
        while le >= 0 and s[le] == s[center]:
            le -= 1
        # expend 2
        while ri < len(s) and le >= 0 and s[le] == s[ri]:
            ri += 1
            le -= 1
        
        return s[le+1:ri]
```