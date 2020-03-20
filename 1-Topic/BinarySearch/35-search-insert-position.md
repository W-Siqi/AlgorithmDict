here is a conclusion: 
1. if we want to find the insert position, use left_bis, the 'start' always points to the result we want
2. if there are duplications of target number, the result could be different by using left_bis or right_bis, but they are all right
solution 1:
```py
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        start, end = 0,len(nums)-1
        while start <= end:
            mid = (start+end)//2
            # in a 'right proritized' way 
            if target <= nums[mid]: end = mid - 1
            else: start = mid + 1
        
        ''' why it is always 'start'
        if start == len(nums):
            # larger than everyone
            return start
        
        if start == 0 and nums[start] != target:
            # smaller than anyone 
            return start
    
        if 0<=start<len(nums)-1:
            if nums[start] == target:
                # find the target
                return start
            else:
                # didn't find the target and it is betwer start and end
                return start
        ''' 
        return start
```

'solution'2:
```py
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
```