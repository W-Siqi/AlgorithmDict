教训：回溯不管有没有影响，都要复原！  
一开始想的是，如果填1个candiate事变，凡是尝试下一个candidate都要覆写的。但是最后一个失败了，是要还原成 '.' 的！
```py
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        empty = [(i,j) for i in range(9) for j in range(9) if board[i][j] == '.']

        def dfs(index):
            if index >= len(empty):
                return True
            
            x,y = empty[index]
            candidates = {chr(ord('0')+i) for i in range(1,10)}
            
            for i in range(9):
                if board[x][i] in candidates:
                    candidates.remove(board[x][i])
                if board[i][y] in candidates:
                    candidates.remove(board[i][y])
            for i in range(3):
                for j in range(3):
                    num = board[(x//3)*3+i][(y//3)*3+j]
                    if num in candidates:
                        candidates.remove(num)
            for candi in candidates:
                board[x][y] = candi
                if dfs(index+1):
                    return True
                else:
                    board[x][y] = '.' 
            return False
        
        dfs(0)
```