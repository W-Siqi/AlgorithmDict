# solution 1 (backtracking)
## Complexity O(N*4^L)
```py
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def BT(board, visited, i,j, word,wordIndex):
            if wordIndex >= len(word):
                return True
            
            target = word[wordIndex]
            
            # try 4 direction
            directions = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
            for x,y in directions:
                # try this direction
                # check boundary
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                    continue
                    
                # if visied 
                if visited[x][y]:
                    continue
                    
                # if matcg target word
                if board[x][y] != target:
                    continue
                
                visited[x][y] = True
                if BT(board,visited,x,y,word,wordIndex+1):
                    return True
                visited[x][y] = False
            
            return False
        
        if not board or not board[0]:
            return False
        
        if len(word) == 0:
            return True

        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    visited = [[False for y in range(len(board[0]))] for x in range(len(board))]
                    visited[x][y] = True
                    if BT(board,visited,x,y,word,1):
                        return True
        
        return False
```

# optimize (space)
1. no need to use visited[][], just use board
2. word + wordIndex can be simpler, just use suffix
```py
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def BT(board, i,j, suffix):
            if len(suffix) == 0:
                return True
            
            target = suffix[0]
            
            # try 4 direction
            directions = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
            for x,y in directions:
                # try this direction
                # check boundary
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                    continue
                    
                # if matcg target word
                if board[x][y] != target:
                    continue
                
                board[x][y] = '^'
                if BT(board,x,y,suffix[1:]):
                    return True
                board[x][y] = target
            
            return False
        
        if not board or not board[0]:
            return False
        
        if len(word) == 0:
            return True

        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    board[x][y] = '#'
                    if BT(board,x,y,word[1:]):
                        return True
                    board[x][y] = word[0]
        
        return False
```