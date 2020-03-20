# 'Back-searching': search from the destination, and mark the place that can reach the destination 
# the natual of this is more like 'dp'... resuse the optimal result..
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        
        # init musk
        muskP,muskA = [],[]
        for line in matrix:
            muskP.append([False]*len(line))
            muskA.append([False]*len(line))
            
        def bfs(matrix,musk,x,y):
            musk[x][y] = True
            
            queue = [(x,y)]
            Nx = len(matrix)
            Ny = len(matrix[0])
            while queue:
                tx,ty = queue.pop(0)
                near = [(tx+1,ty),(tx-1,ty),(tx,ty+1),(tx,ty-1)]
                for nx,ny in near:
                    within =  nx >= 0 and nx < Nx and ny >= 0 and ny < Ny
                    if within and not musk[nx][ny] and matrix[nx][ny] >= matrix[tx][ty]:
                        queue.append((nx,ny))
                        musk[nx][ny] = True
        
        sizex = len(matrix)
        sizey = len(matrix[0])
        # BFS from pacific
        for i in range(sizex):
            bfs(matrix,muskP,i,0)
        for i in range(sizey):
            bfs(matrix,muskP,0,i)
        # BFS from Atlantic
        for i in range(sizex):
            bfs(matrix,muskA,i,sizey-1)
        for i in range(sizey):
            bfs(matrix,muskA,sizex-1,i)
        
        # resuilt querying 
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if muskA[i][j] == True and muskP[i][j] == True:
                    res.append([i,j])
                    
        return res