two-pointers version:
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height) - 1
        while(l<r):
            res = max(res,min(height[r], height[l])*(r-l))
            if(height[l]>height[r]):
                r -= 1
            else:
                l += 1
        return res
```

alpha-beta verson 1:
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        h = 0
        for i in range(len(height)):
            # move forward means width become shorter
            # if the heiht become even shorter, then it is not promising 
            if(height[i]>h):
                h = height[i]
            else:
                continue
                
            if height[i]*(len(height)-1-i) < res:
                continue
                
            for j in range(i+1,len(height)):
                res = max(res,min(height[i],height[j])*(j-i))
        return res
```

alpha-beta version2:
```python 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        h = 0
        for i in range(len(height)):
            if(height[i]>h):
                h = height[i]
            else:
                continue
            
            hr = 0
            for j in range(len(height)-1,i,-1):
                if(height[j]>hr):
                    hr = height[j]
                    res = max(res,min(height[i],height[j])*(j-i))
                else:
                    continue
                
                # if it has already beyond another height, then no need to shink width to get larger height
                if(hr > height[i]):
                    break    
                    
        return res
```