# hash 当做bucket...
```py
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        buckets = [True] * n
        buckets[0],buckets[1] = False,False
        res = 0
        curNum = 2
        while curNum < n:
            res += 1
            fillNum = curNum
            while fillNum < n:
                buckets[fillNum] = False
                fillNum += curNum
            while curNum < n and not buckets[curNum]:
                curNum += 1
        return res
```