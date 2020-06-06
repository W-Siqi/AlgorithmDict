# DP
## 为什么gird走格子基本就是DP的高发区？
- 因为走步子的决策树DFS下去，是指数的复杂度，不用DP基本就是要爆炸。
- 最优解子结构，走到这位置，我们只在乎值是多少，往往不在乎是怎么走过来的

## 这题的状态定义
1. 最暴力的，就是四个状态d[a][b][c][d] 表示两个机器人的坐标。  
2. 但是因为是一直向前走的，我可以把一个定义为“问题规模”，即走到第几行位置。所以就剩3个状态了d[row][a][b]  
3. 还能进一步优化，我们可以只考虑a < b，因为一旦a > b 我们可能吧两个机器人置换位置，这是等价的

## 这题的 Implementation
一个是这里9个前驱可千万别九个if/else，之前说了，类似的逻辑结构用for+target list  
另一个是查询前驱状态用hash存储，好处有2：
1. 节省空间，用二维的grid会有很多空的
2. 实现简单，是否存在，用hash是最容易判定的，而且是O（1）
```py
class Solution(object):
    def cherryPickup(self, grid):
        def ha(i,j):
            return str(i)+'-'+str(j)
        
        rows,cols = len(grid),len(grid[0])
        dp = [{}]
        dp[0][ha(0,cols-1)] = grid[0][0]+grid[0][-1]
        for i in range(1,rows):
            dp.append({})
            for a in range(cols):
                for b in range(a+1,cols):
                    pres = [ha(a,b-1),ha(a,b),ha(a,b+1),
                            ha(a-1,b-1),ha(a-1,b),ha(a-1,b+1),
                            ha(a+1,b-1),ha(a+1,b),ha(a+1,b+1)]
                    candidates = []
                    for pre in pres:
                        if pre in dp[i-1]:
                            candidates.append(dp[i-1][pre]+grid[i][a]+grid[i][b])
                    if candidates:
                        dp[i][ha(a,b)] = max(candidates)
        return max(dp[-1].values())
        
```