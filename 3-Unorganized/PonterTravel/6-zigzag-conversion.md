```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows < 0:
            return ""
        if numRows == 1:
            return s
        
        lines = [""]*numRows
        isDown = True
        curL = 0
        for char in s:
            # add to line
            lines[curL] += char
            
            # move to next line
            if isDown:
                curL += 1
                if curL >= numRows:
                    curL -= 2
                    isDown = False
            else:
                curL -= 1
                if curL < 0:
                    curL += 2
                    isDown = True
        
        res = ""
        for line in lines:
            res += line
            
        return res
```      