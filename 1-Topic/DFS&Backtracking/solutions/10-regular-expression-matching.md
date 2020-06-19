# 策略搜索时DP不DP？
最优子结构是存在的，dp[i][j] ture or false  
但是有重复的子结构吗？  
其实除了a * a * a * a *b这种情况，是不怎么有重复的子结构出现的。所以有两种方案   
1. 把a * 的等价掉（solution1）  
2. 用memorization 来进行DP

## 这题的edgecase
这题，难在各种特例没想明白，  
wrong answer记录：
# solution 1: Backtracking
```py
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        def match(si,pi):
            if si >= len(s) and pi >= len(p):
                return True
            elif pi >= len(p) and si < len(s):
                return False
            elif pi < len(p) and si >= len(s):
                while pi < len(p):
                    if pi+1 < len(p) and p[pi+1] == '*':
                        pi += 2
                    else:
                        return False
                return True
            
            if pi+1 < len(p) and p[pi+1] == '*':
                if s[si] == p[pi] or p[pi] == '.':
                    return match(si,pi+2) or match(si+1,pi+2) or match(si+1,pi)
                else:
                    return match(si,pi+2)
            elif s[si] == p[pi] or p[pi] == '.':
                return match(si+1,pi+1)
            else:
                return False

        i,newp =0, ""
        while i < len(p):
            if i+3 < len(p) and p[i+1] == '*'and p[i+2] == p[i] and p[i+3] == '*':
                i+=2            
            else:
                newp += p[i]
                i+=1
        p = newp
        
        return match(0,0)
```