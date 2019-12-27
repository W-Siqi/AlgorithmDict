class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def pathSearch(i,j,matrix):
            # mark '-1' when visited
            visited={(i,j)}
            queue = [(i,j)]
            depth = 0
            maxi = len(matrix) - 1
            maxj = len(matrix[0]) - 1
            while queue:
                # update to next layer
                for count in range(len(queue)):
                    topi,topj = queue.pop(0)
                    # try add 4 direction 
                    candidates = [(topi+1,topj),(topi-1,topj),(topi,topj+1),(topi,topj-1)]
                    for ci,cj in candidates:
                        if ci >= 0 and ci <= maxi and cj>=0 and cj <= maxj and (ci,cj) not in visited:
                            if(matrix[ci][cj] == 0):
                                return depth + 1
                            visited.add((ci,cj))
                            queue.append((ci,cj))
                depth += 1
                
            return 0
        
        
        res = matrix[:]
        for i in range(len(res)):
            for j in range(len(res[i])):
                if res[i][j] == 1:
                    res[i][j] = pathSearch(i,j,matrix)
        return res