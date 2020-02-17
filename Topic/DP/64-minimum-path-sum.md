```py
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                hori, verti = float("inf"), float("inf")
                if i-1 >= 0:
                    verti = grid[i-1][j]
                if j-1 >= 0:
                    hori = grid[i][j-1]
                # skip the grid[0][0]
                if not (i==0 and j == 0):
                    grid[i][j] += min(hori,verti)
        
        return grid[-1][-1]
```