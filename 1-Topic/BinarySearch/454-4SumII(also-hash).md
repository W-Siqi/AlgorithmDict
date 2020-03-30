# key&tag
hash, cache, bs
# lession:
edge case，我忘记考虑BS的序列是可以重复的

# solution1（最优）: hash
### 简介的写法，collactions.counter
```py
    hashAB = collections.Counter([a+b for a in A for b in B])

    # 不然的话..
    hashAB = []
    for ab in [a+b for a in A for b in B]:
        if ab in hashAB:
            hashAB[ab] += 1
        else:
            hashAB[ab] = 1
```

```py
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hashAB = collections.Counter([a+b for a in A for b in B])
        res = 0
        for cd in [c+d for c in C for d in D]:
            res += hashAB.get(-cd,0)
            
        return res
```

# solution2：cache + binary search
```py
# wrong answer, duplicate ！
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = sorted([a+b for a in A for b in B])
        CD = sorted([c+d for c in C for d in D])
        res = 0
        for ab in AB:
            # find lower bound -ab in cd
            # find upper bound
            lo, hi = 0, len(CD) - 1
            while lo < hi:
                mid = (lo + hi)//2
                if CD[mid] < -ab:
                    lo = mid + 1
                else:
                    hi = mid
            lower = lo
            
            lo, hi = 0, len(CD) - 1
            while lo < hi:
                mid = (lo + hi + 1)//2
                if CD[mid] > -ab:
                    hi = mid - 1
                else:
                    lo = mid
            upper = hi
            if CD[lower] == -ab:
                res += (upper - lower + 1)
            
        return res
```

