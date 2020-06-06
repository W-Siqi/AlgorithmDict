# Hash
我一开始看k的规模，去查询这么长的一个里面的substring，是要爆炸。  
后来发现查询的target是定长的  
然后就很类似[1044-longest-duplicate-substring](./1-Topic/Hash/solutions/1044-longest-duplicate-substring.md).  
对定长的窗口跑一遍hash。   

所以还是意识两个点：
1. 频繁查询用hash
2. 定长substring的查询hash值计算
```py
class Solution(object):
    def hasAllCodes(self, s, k):
        if len(s) < k:
            return False
        
        numset = set()
        num = 0

        font = pow(2,k-1)
        for i in range(len(s)):
            if i-k >= 0 and s[i-k] == '1': num -= font
            num = num*2
            if s[i] == '1': num += 1
            if i >= k-1: numset.add(num)
        
        return len(numset) == pow(2,k)
```