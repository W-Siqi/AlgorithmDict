# solution 1 (DFS)
```py
class Solution:
    def hasValidPath(self,grid):
        def DFS(gird,x,y,visited):
            if x == m-1 and y == n - 1:
                return True
            
            # find all directions can go:           
            directions = []
            # get direction accroding to its type
            candidates = outDir[grid[x][y]]
            for d in candidates:
                nx, ny = x + dirOffset[d][0], y + dirOffset[d][1]
                
                # del direction if next is out of range
                if nx < 0 or nx >= m  or ny < 0 or ny >= n:
                    continue
                    
                # del direction in visited
                if (nx,ny) in visited:
                    continue
                    
                # del direction if nextcan not connect
                nextType = grid[nx][ny]
                eDirs = enterDir[nextType]
                if d not in eDirs:
                    continue
                
                directions.append(d)
            
            for d in directions:
                visited.add((x,y))
                if DFS(grid,x+dirOffset[d][0],y+dirOffset[d][1],visited):
                    return True
                visited.pop()
            
            return False
        
        # 使用映射关系，避免if，只需要遍历就可以了
        dirOffset = [(0,-1),(-1,0),(0,1),(1,0)]
        outDir = {1:[0,2],2:[1,3],3:[0,3],4:[3,2],5:[1,0],6:[1,2]}
        enterDir = {1:[0,2],2:[3,1],3:[2,1],4:[1,0],5:[3,2],6:[3,0]}

        m,n = len(grid),len(grid[0])
        visited = set()
        return DFS(grid,0,0,visited) 
```

# solution 2 BFS
```py
class Solution(object):
    def hasValidPath(self, grid):
        outs = {(1,-8),(1,8),(2,-6),(2,6),(3,8),(3,6),(4,-8),(4,6),(5,-6),(5,8),(6,-6),(6,-8)}
        m,n = len(grid),len(grid[0])
        seen = {(0,0)}
        queue = [(0,0)]
        dirs = [(-1,0,-6),(1,0,6),(0,-1,8),(0,1,-8)]

        while queue:
            font = queue.pop(0)
            for d in dirs:
                nei = (d[0]+font[0],d[1]+font[1])
                within = nei[0] >= 0 and nei[0] < m and nei[1] >= 0 and nei[1] < n
                # chack if within and if seen before
                if within and nei not in seen:
                    # check if can reach
                    fonttype,neitype = grid[font[0]][font[1]],grid[nei[0]][nei[1]]
                    if (fonttype,d[2]) in outs and (neitype,-d[2]) in outs:
                        seen.add(nei)
                        queue.append(nei)
        return (m-1,n-1) in seen
```