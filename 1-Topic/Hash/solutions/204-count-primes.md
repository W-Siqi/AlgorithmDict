# motivation
这题还是挺特殊的，把hash 当做bucket...   
但是，当int/自然数 当做元素集合的时候，确实hash就是个原生的好帮手，int本身作为下标就是个完美的hash，这个在很多题目里面都见过。
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