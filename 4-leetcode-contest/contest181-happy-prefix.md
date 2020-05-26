# Key words
KMP, Rabin-Karp

# naive solution
O(n*n)是很容易的
```py
class Solution:
    def longestPrefix(self, s: str) -> str:
        res = ""
        curPos = 1
        
        while curPos < len(s):
            if len(s) - curPos <= len(res):
                break
            
            # look for the first letter match start 
            while curPos < len(s) and s[curPos] != s[0]:
                curPos += 1
            
            if curPos < len(s):
                isMatch = True
                # try match the string start from curPos
                for i in range(len(s)-curPos):
                    if s[curPos + i] != s[i]:
                        isMatch = False
                        break
                
                if isMatch and len(s) - curPos > len(res):
                    res = s[curPos:]
            
            curPos += 1
            
        return res
```

# hash
我们比较字串的时候，计算一个hash 值。只要比较hash值是否相等。   
Rabin-Karp hash: 
https://www.cnblogs.com/golove/p/3234673.html  
其特点是，头部和尾部的添加，是O(1)的。  

## 关于hash溢出
1- 使用大数mod 10^9+7  
2- pow(128,n) 的时候， 换成pow(128,n,mod)，因为字符串长度上千也不是不可以，这样计算pow时间直接爆掉。

```py
class Solution:
    def longestPrefix(self, s: str) -> str:
        preHash,sufHash,mod = 0,0,10**9+7
        
        res = 0
        for i in range(len(s)-1):
            preHash += ord(s[i])*pow(128,i,mod)
            preHash %= mod
            sufHash = sufHash * 128 + ord(s[-(i+1)]) 
            sufHash %= mod
            
            if preHash == sufHash:
                res = max(res,i+1)
            
            
        return s[:res]
```

# KMP
等着填坑