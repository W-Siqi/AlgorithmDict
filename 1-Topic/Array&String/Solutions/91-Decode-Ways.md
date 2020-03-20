# solution1
```py
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]*(len(s)+2)    
        dp[-1] = 0
        for i in range(len(s)-1,-1,-1):
            
            if s[i] == '0':
                dp[i] = 0   
            elif s[i] == '1':
                dp[i] = dp[i+1] + dp[i+2]
            elif s[i] == '2':
                if i+1 < len(s) and s[i+1] <= '6':
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
            else:
                dp[i] = dp[i+1]
                
        return dp[0]
```