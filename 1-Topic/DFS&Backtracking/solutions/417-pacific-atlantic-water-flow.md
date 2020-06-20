# grid 点到区域寻径，寻通路
这题DFS直接做会超时，因为这题对每个点都进行一次寻径，有很多重叠的子问题。  
解决方案：
1. DFS+momorization ，类似于top-down DP的思想
2. 从区域开始反向用BFS进行4连通填充
# solution 1 : DFS+momorization
```py
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m,n = len(matrix),len(matrix[0])
        memoP = {}
        memoA = {}
        def dfs(x,y,path,isPaci):
            # print(x,y)
            if x < 0 or y < 0:
                return isPaci
            if x >= m or y >= n:
                return not isPaci
            
            memo = memoP if isPaci else memoA
            key = (x,y)
            if key in memo:
                return memo[key]
            
            path = path+[(x,y)]
            nextPos = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            for p in nextPos:
                if p[0] >= 0 and p[0] < m and p[1] >= 0 and p[1] < n and matrix[p[0]][p[1]] > matrix[x][y]:
                    continue
                if p in path:
                    continue
                if dfs(p[0],p[1],path,isPaci):
                    for validP in path:
                        memo[validP] = True
                    return True
                
            #memo[key] = False
            return False
        
        res = []
        for x in range(m):
            for y in range(n):
                if dfs(x,y,[],True) and dfs(x,y,[],False):
                    res.append([x,y])
        return res
```

# solution 2: BFS
