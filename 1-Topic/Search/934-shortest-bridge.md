# 区域对区域的寻径
就是从其中一个区域的边缘开始扩张
# solution 1 从边缘开始BFS
```py
class Solution(object):
    def shortestBridge(self, A):
        def getIslandEdges(cx,cy):
            res = []
            q = [(cx,cy)]
            while q:
                font = q.pop(0)
                seen.add(font)
                for d in dirs:
                    nei = (d[0]+font[0],d[1]+font[1])
                    if nei[0] >= 0 and nei[0] < m and nei[1] >= 0 and nei[1] < n:
                        if A[nei[0]][nei[1]] == 0 and font not in res:
                            res.append((font[0],font[1],0))
                        elif A[nei[0]][nei[1]] == 1 and nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            return res
                
        m,n = len(A),len(A[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = []
        seen = set()
        
        # add edges
        for x in range(m):
            for y in range(n):
                if A[x][y] == 1 and not queue:
                    queue = getIslandEdges(x,y)

        while queue:
            top = queue.pop(0)
            for d in dirs:
                nei = (d[0]+top[0],d[1]+top[1])
                if nei[0] >= 0 and nei[0] < m and nei[1] >= 0 and nei[1] < n and nei not in seen:
                    seen.add(nei)
                    if A[nei[0]][nei[1]] == 1:
                        return top[2]
                    else:
                        queue.append((nei[0],nei[1],top[2]+1))
        return -1
```

# solution 2 对solution1代码简洁
首先get neiboorhood抽出函数，避免超长的if和嵌套。  
其次，找boundary，用dfs写更简洁一些。纯写法上而言，dfs往往比bfs舒服。
```py
class Solution(object):
    def shortestBridge(self, A):
        m,n = len(A),len(A[0])
        
        def getNeis(x,y):
            res = []
            for nei in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if nei[0] >= 0 and nei[0] < m and nei[1] >= 0 and nei[1] < n:
                    res.append(nei)
            return res 
        
        def getBounds(cx,cy):
            seen.add((cx,cy))
            for nei in getNeis(cx,cy):
                if A[nei[0]][nei[1]] == 0 and (cx,cy) not in queue:
                    queue.append((cx,cy,0))
                elif A[nei[0]][nei[1]] == 1 and nei not in seen:
                    getBounds(nei[0],nei[1])
                
        queue = []
        seen = set()

        for x in range(m):
            for y in range(n):
                if A[x][y] == 1 and not queue:
                    getBounds(x,y)

        while queue:
            top = queue.pop(0)
            for nei in getNeis(top[0],top[1]):
                if nei not in seen:
                    seen.add(nei)
                    if A[nei[0]][nei[1]] == 1:
                        return top[2]
                    else:
                        queue.append((nei[0],nei[1],top[2]+1))
        return -1
```