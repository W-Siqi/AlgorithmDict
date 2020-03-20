the first thought is to use two poiners,   
however, since the start must  == end, at next turn.  
we can have quicker one way traverse:a
```py
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # rank 
        intervals.sort(key = lambda x:x[0])
        # two pointer traverse
        res = [intervals[0]]
        for small,big in intervals:
            if small <= res[-1][1]:
                res[-1][1] = max(res[-1][1],big)
            else:
                res.append([small,big])
        return res
```