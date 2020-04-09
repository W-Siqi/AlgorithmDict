# solution 1
没啥好说的，就是个二分找lower bound
```py
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()      
        radius = 0
        for h in houses:
            lo,hi = 0, len(heaters)
            while lo < hi:
                mid = (lo+hi)//2
                if heaters[mid] < h:  lo = mid + 1
                else: hi = mid
    
            left = heaters[lo-1] if lo-1>=0 else -float("inf")
            right = heaters[lo] if lo < len(heaters) else float("inf")
            radius = max(radius, min(h-left,right-h))
        return radius
```