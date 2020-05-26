# slding window 
这题初始写法，比较复杂。我把他分成两个阶段了： 
1. 扩张到k长度
2. 接下来每增加一个头，就减去一个尾巴  
当时花了些时间查了下bug，因为两个阶段之间会有edgecase，比如一字符总共就比k短怎么办？  
（**因此，简化逻辑，也是避免bug的很好的一个办法！**）
```py
class Solution(object):
    def maxVowels(self, s, k):

        res = 0
        number = 0
        counter = k
        for i in range(min(len(s),k)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' :
                number += 1
        
        res = number
        while counter < len(s):
            i = counter
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' :
                number += 1
            i = counter - k
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' :
                number -= 1
            res = max(res,number)
            counter += 1
        return res
```
后来的写法，就把他当做sliding window，每次end往前推，如果发现长度长了，就减去尾巴。这样就不用分两个阶段两段代码了
```py
class Solution(object):
    def maxVowels(self, s, k):
        def isVowel(c):
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'
        
        res,curNum,end = 0,0,0
        while end < len(s):
            if isVowel(s[end]): curNum += 1
            if end >= k and isVowel(s[end - k]): curNum -= 1
            res = max(res,curNum)
            end += 1
        return res
```