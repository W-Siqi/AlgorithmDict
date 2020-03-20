
solution1:
``` python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start,end = 0,len(nums)
        tarInd = -1
        while start < end:
            md = (start+end)//2
            if nums[md] == target:
                tarInd = md
                break
            elif nums[md] > target:
                end = md
            else:
                start = md + 1
        
        if tarInd == -1:
            return [-1,-1]
        
        l = r = tarInd
        while l-1>=0 and nums[l-1]==target:
            l-=1
        while r + 1<len(nums) and nums[r+1]==target:
            r+=1
        return [l,r]
```

solution2: 
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        # for left
        start,end = 0,len(nums)-1
        while start <= end:
            md = (start+end)//2
            if target <= nums[md]: end = md - 1
            else: start = md + 1
        left = start if 0 <= start < len(nums) and nums[start] == target else -1
        
        if left == -1:
            return [-1,-1]
        
        # for right
        start,end = 0,len(nums)-1
        while start <= end:
            md = (start+end)//2
            if target >= nums[md]: start = md + 1
            else: end = md - 1
        right = end if 0 <= end < len(nums)  and nums[end] == target else -1
        
        return [left,right]
```