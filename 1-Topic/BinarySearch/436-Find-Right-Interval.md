 # Key&tag
 其实就是bs找upper bound，  
 solution主要强调怎么用py写简洁的代码

 # soluiton
### 第一处, 用for 来创建list
```py
    # 原本方案
    sorted_start_val = []
    for index,interval in enumerate(intervals):
        sorted_start_val.append([interval[0],index])
    sorted_start_val.sort(key = lambda x:x[0])

    # 简洁版
    sorted_start_val = [[I[0], i] for i, I in enumerate(intervals)]
    sorted_start_val.sort(key = lambda x:x[0])
```
### 第二处, py的 bisect. （当然，这个实现也是需要会写的！）
```py

```

### 第三处,通过缺省值避免if讨论边界值
```py
```
### 
```py
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        res = [-1]*N
        
        sorted_start_val = [[I[0], i] for i, I in enumerate(intervals)]
        sorted_start_val.sort(key = lambda x:x[0])
        
        for i in range(N):
            # find upper bound in BS
            target,lo,hi = intervals[i][1],0,N-1
            while lo < hi:
                mid = (lo + hi)//2
                if sorted_start_val[mid][0] < target:
                    lo = mid + 1
                else:
                    hi = mid
            
            # avoid self
            j = lo
            while j < N and (sorted_start_val[j][1] == i or sorted_start_val[j][0] < target):
                j += 1
            if j < N:
                res[i] = sorted_start_val[j][1] 
                
        return res
```

