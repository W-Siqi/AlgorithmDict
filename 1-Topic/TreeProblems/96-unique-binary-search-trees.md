# BST&DP
这题就是要了解，怎么从序列构造BST  
至于dp的动机，是因为重复子结构太明显了，和裴波那契数列一样
# solution
```py
class Solution(object):
    def numTrees(self, n):
        dp = [0]*(n+1)
        dp[0],dp[1] = 1,1
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j] 
        return dp[-1]
```