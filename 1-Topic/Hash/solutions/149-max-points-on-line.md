这题，主要一个明白，判直线的方法。  
另外，注意这题的edge case。 以及高精度的解决方案-直接用string-decimal来编码数字

# solution
```py
# edge case： 重复，以及点的个数为1
# edge case： 精度不行
from decimal import *

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        res = 1
        for i in range(len(points)):
            slope = {}
            same = 0
            for j in range(len(points)):
                if i == j:
                    continue
                    
                p1,p2 = points[i],points[j]
                if p1[0] == p2[0] and p1[1] == p2[1]:
                    same+=1
                else:
                    s = Decimal(p2[1]-p1[1])/Decimal(p2[0]-p1[0]) if p2[0] != p1[0] else float("inf")
                    if s not in slope:
                        slope[s] = 1
                    else:
                        slope[s] += 1
            if len(slope.keys()) == 0:
                res = max(res,same+1)
            else:
                res = max(res,same+max(slope.values())+1)
            print(slope,same)
        return res
```