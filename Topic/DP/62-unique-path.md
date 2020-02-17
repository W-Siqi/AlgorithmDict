```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
                
        dp = [[0 for a in range(n)] for a in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j -1 >= 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]
```