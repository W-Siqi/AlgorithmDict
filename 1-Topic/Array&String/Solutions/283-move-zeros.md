# tag
a smart trick to remove  element in-place in array
# solution
```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i,num in enumerate(nums):
            nums[i-count] = num
            if num == 0:
                count += 1
        for i in range(count):
            nums[-(i+1)] = 0
        
```
