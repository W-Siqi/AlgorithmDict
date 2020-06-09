# DP
3个维度。  
第一个维度，问题规模，一位数组的情形很常见。  
另外两个维度，color和target数，都是为了状态转移必须知道的信息。
# debug最多的地方:初始值的设定
不管是bottom-up 还是 top-down 都避免不了这个问题。  
一个是非法值返回inf，另一个是启动值要返回0   
# 写法 bottom-up 和 top-down
其实top-down更思路清晰一点...  
用hash 缓存最优子结构，更接近dp的实质，而且剩空间。  
### 这题Bottom UP 难写的实质：
3D的DP，你循环更新就已经是3层循环，如果更新的时候需要遍历，那么循环套循环，代码会很难看。
## top-down
```py
class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        #[house][color][target]
        dp = {}
        
        def dfs(hou,col,target):
            if target > hou or target < 0 or (target == 0 and hou > 0):
                return float("inf")
            if hou == 0:
                return 0
       
            key = (hou,col,target)              
            if key not in dp:
                res = float("inf")
                if houses[hou-1] == 0:
                    for c in range(1,n+1):
                        if c ==col: 
                            res = min(res,dfs(hou-1,c,target)+cost[hou-1][col-1])
                        else:
                            res = min(res,dfs(hou-1,c,target-1)+cost[hou-1][col-1])
                elif houses[hou-1] == col:
                     for c in range(1,n+1):
                        if c == houses[hou-1]: 
                            res = min(res,dfs(hou-1,c,target))
                        else:
                            res = min(res,dfs(hou-1,c,target-1))
                dp[key] = res
                
            return dp[key]
             
        res = float("inf")
        for col in range(1,n+1):
            res = min(res,dfs(m,col,target))

        if res == float("inf"): return -1
        else: return res
```
## bottom-up
```py
class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        #[house][color-1][target-1]
        dp = [[[float("inf") for k in range(target)]for j in range(n)]for i in range(m)]
        
        # init 
        if houses[0] == 0:
            for col in range(1,n+1):
                dp[0][col-1][0] = cost[0][col-1]
        else:
            dp[0][houses[0]-1][0] = 0
        
        # update
        for i in range(1,m):
            if houses[i] == 0:
                # try all color
                for col in range(1,n+1):
                    # try all targets num
                    dp[i][col-1][0] = dp[i-1][col-1][0]+cost[i][col-1]
                    for tar in range(1,target):
                        # track all precol
                        for precol in range(1,n+1):
                            if precol == col:
                                dp[i][col-1][tar] = min(dp[i][col-1][tar],dp[i-1][precol-1][tar]+cost[i][col-1])
                            else:
                                dp[i][col-1][tar] = min(dp[i][col-1][tar],dp[i-1][precol-1][tar-1]+cost[i][col-1])
                                
            else:
                # only this color
                col = houses[i]
                # try all targets num
                dp[i][col-1][0] = dp[i-1][col-1][0]
                for tar in range(1,target):
                    for precol in range(1,n+1):
                        if precol == col:
                            #print(i,col,tar,"precol",precol,"pretar",tar,dp[i-1][precol-1][tar])
                            dp[i][col-1][tar] = min(dp[i][col-1][tar],dp[i-1][precol-1][tar])
                        else:
                            #print(i,col,tar,"precol",precol,"pretar",tar-1,dp[i-1][precol-1][tar-1])
                            dp[i][col-1][tar] = min(dp[i][col-1][tar],dp[i-1][precol-1][tar-1])
        
        res = float("inf")
        for col in range(1,n+1):
            res = min(res,dp[-1][col-1][-1])
        if res == float("inf"):
            return -1
        else:
            return res
```