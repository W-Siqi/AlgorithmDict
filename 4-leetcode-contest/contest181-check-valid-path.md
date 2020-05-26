# Key words
**graph的寻径**, **DFS** 

和标准的 grid map 寻径不一样的是， next step 的判定函数有点恶心

# 使用映射 来避免 一万个if
这题唯一的难点，就是优雅的用map和musk的技巧，避免写一万个if  
多层if，一个容易出错，二个时间很长，很浪费写题时间， 最重要的是显得你很蠢！  

# graph 的 visited, 隐藏的O()
这题，按道理是O(mn). 活生生得被我写成O(mn*mn)  
因为visited我是用的list，这样for (x,y) in visited 就是O(m,n)了.  
**LESSION:**  
**graph的visited，频繁查找的，一定要用hashmap来存储，不然节点一多直接爆炸，而且这题我还没意识到**
# solution
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