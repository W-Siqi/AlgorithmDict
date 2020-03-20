```py
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        lo = max(weights)   
        hi = sum(weights)
        while lo < hi:
            mid  = (lo + hi) // 2
            
            # calculate days
            day, cur = 1,0
            for w in weights:
                if cur + w <= mid:
                    cur += w
                else:
                    day += 1
                    cur = w
  
            if day > D: # mid is too small
                lo = mid + 1
            else: # mid is too big, can be smaller
                hi = mid
                
        return lo
```