# 排列组合的 枚举VS计数VS最优组合
这题是一个典型的枚举问题，简简单单的按照DFS搜进去就行了。  
枚举问题最简单，因为无法优化，O(k^N)就是最优解，你是要把所有的都枚举出来啊。  
而计数问题和最优组合，就可能要涉及DP等技巧了
```py
class Solution(object):
    def letterCombinations(self, digits):
        phone = [('a','b','c'),('d','e','f'),('g','h','i'),('j','k','l'),('m','n','o'),('p','q','r','s'),('t','u','v'),('w','x','y','z')]
        res = []
        def dfs(digits,index,preStr):
            if index >= len(digits):
                res.append(preStr)
                return 
            choices = phone[ord(digits[index])-ord('2')]
            for c in choices:
                dfs(digits,index+1,preStr+c)
                
        if not digits:
            return res
        dfs(digits,0,"")
        return res
            
            
```