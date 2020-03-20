# common bug - 'change element in dynamic for'
set the column and row **whenever meet zero**  
in this way, you will create 'fake zero', which is set by you but will cause zero setting. 

```py
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = []
        columns = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
                    
        for row in rows:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0
        
        for column in columns:
            for i in range(len(matrix)):
                matrix[i][column] = 0
            
```