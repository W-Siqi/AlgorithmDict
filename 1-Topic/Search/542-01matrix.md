# 点到区域寻径
反向填充，类似leetcode 417
```py
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(matrix),len(matrix[0])
        queue = [(x,y,0) for x in range(m) for y in range(n) if matrix[x][y] == 0]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        seen = {(q[0],q[1]) for q in queue}
        
        while queue:
            top = queue.pop(0)
            # fill distance
            matrix[top[0]][top[1]] = top[2]
            # extend neibors
            for d in dirs:
                nei = (top[0]+d[0],top[1]+d[1])
                if nei[0] < m and nei[0] >= 0 and nei[1] >= 0 and nei[1] < n and nei not in seen:
                    seen.add(nei)
                    queue.append((nei[0],nei[1],top[2]+1))
                    
        return matrix
```