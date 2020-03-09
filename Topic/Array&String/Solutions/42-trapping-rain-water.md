# solition 1 (cache max)
```py

class Solution:
    def trap(self, height: List[int]) -> int:
        sumWater = 0
        lMax, rMax = [-1]*len(height), [-1]*len(height)
        
        maxH = -1
        for i,h in enumerate(height):
            maxH = max(maxH,h)
            lMax[i] = maxH
            
        maxH = -1     
        for i in range(len(height)-1,-1,-1):
            maxH = max(maxH,height[i])
            rMax[i] = maxH
        
        for i in range(len(height)):
            h = height[i]
            top = min(lMax[i],rMax[i])
            sumWater += (top - h)
            
        return sumWater
    
```

# solution2 (two-pointers)： space O(n)->O(1)
```py
class Solution:
    def trap(self, height: List[int]) -> int:
        sumWater = 0
        lmax,rmax = -1,-1
        l,r = 0,len(height)-1
        while l <= r:
            if lmax > rmax:
                # add to sumWater
                sumWater += max(0,rmax - height[r])
                # update the rmax
                rmax = max(rmax,height[r])
                # move right pointer
                r -= 1
            else:
                # add to sumWater
                sumWater += max(0,lmax-height[l])
                # update the lmax
                lmax = max(lmax,height[l])
                # move light pointer
                l += 1
                
        return sumWater
```