# solution 1:
to make code concise, use looping queue four_dirs to control the directioon change, to avoid '4 if else'

when change direction? when cannot move: reach some place visited or index out of the matrix
```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:   
        def isIndexValid(x,y):
            if x >= 0 and x < len(matrix) and y >=0 and y < len(matrix[0]):
                return True
            else:
                return False
            
        if not matrix or not matrix[0]:
            return []
        
        
        res = []
        four_dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        cur_dir = 0
        cur_pos = [0,-1]
        total = len(matrix)*len(matrix[0])
        visited = set()
        while(len(res) < total):
            nextPos = [cur_pos[0]+four_dirs[cur_dir][0],cur_pos[1]+four_dirs[cur_dir][1]]
            # check validation
            if isIndexValid(nextPos[0],nextPos[1]) and tuple(nextPos) not in visited:
                # valid: move to and visit
                res.append(matrix[nextPos[0]][nextPos[1]])
                visited.add(tuple(nextPos))
                cur_pos = nextPos
            else:
                # in valid: change direction
                if cur_dir == 3:
                    cur_dir = 0
                else:
                    cur_dir += 1
        
        return res
```