# solution 
try strategy，试探  模型
```py
class Solution:
    def arrangeCoins(self, n: int) -> int:
        def isEnough(stairs,coins):
            return (1+stairs)*stairs/2 <= coins
        
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if isEnough(mid,n):
                # can be bigger
                if mid == lo:
                    return hi if isEnough(hi,n) else lo
                else:
                    lo = mid
            else:
                # so big for now
                hi = mid - 1
        return lo
```