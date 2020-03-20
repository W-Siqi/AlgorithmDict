# solution1 O(N)
```py
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return i
        
        return len(nums) - 1
```

# solution2 O(logN)
the basic idea is that, even if it is not peak, we can know the tendency
```py
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
          
        while start < end:
            mid  = (start + end) // 2
            leftNum = nums[mid - 1] if mid > 0 else -float("inf")
            rightNum = nums[mid + 1] if mid < len(nums)-1 else -float("inf") 
            
            # is peak
            if nums[mid] > leftNum and nums[mid] >rightNum:
                return mid
            # is increasing 
            elif leftNum  < nums[mid] and nums[mid] < rightNum:
                start = mid + 1
            # is decreasing 
            elif leftNum  > nums[mid] and nums[mid] > rightNum:
                end = mid - 1
            # is bottom
            else:
                start = mid + 1
        
        return start
```