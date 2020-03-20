# mistake in python
```py
# the result would be float!!!
mid = (low + high)/2  

# should write like this:
mid = int((low + high)/2)
```
```py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m,n = len(matrix),len(matrix[0])
        low , high = 0, m*n-1
        while low < high:
            mid = int((low + high) / 2)
            i,j = divmod(mid,n)
            if matrix[i][j] > target:
                high = mid - 1
            elif matrix[i][j] < target:
                low = mid + 1
            else:
                return True
        
        i,j = divmod(low,n)
        if matrix[i][j] == target:
            return True
        else:
            return False       
```