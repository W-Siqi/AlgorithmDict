# solution 1 DFS
```py
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:     
        def DFS(s1,s2,s3,p1,p2,p3):
            if p3 >= len(s3):
                return True
            # try to move s1
            if p1 < len(s1) and s1[p1] == s3[p3] and  DFS(s1,s2,s3,p1+1,p2,p3+1):
                return True
            # try to move s2
            if p2 < len(s2) and s2[p2] == s3[p3] and DFS(s1,s2,s3,p1,p2+1,p3+1):
                return True
            # fail, trun false
            return False
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        return DFS(s1,s2,s3,0,0,0)
```

# solution 2 DP
```py
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:     
        dp = [[False for x in range(len(s2)+1)]for x in range(len(s1)+1)]
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp[0][0] = True
        for i in range(0,len(dp)):
            for j in range(0,len(dp[0])):
                if i == 0 and j == 0:
                    continue 
                    
                # try dp[i-1][j]
                if dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                # try dp[i][j-1]
                elif dp[i][j-1] and s2[j-1] ==s3[i+j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[-1][-1]
```