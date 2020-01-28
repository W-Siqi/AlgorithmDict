solution1: find the smallest bigger, an then rank 
```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        exchanged = False
        for i in range(len(nums)-1,-1,-1):
            win = -1
            smallest = 999
            # try to find smallest bigger number
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i] and nums[j] < smallest:
                    win = j
                    smallest = nums[j]
            
            if win > 0:
                # found it !
                # swap 
                nums[i], nums[win] = nums[win],nums[i]
                 # rank from i+1 to last
                nums[i+1:len(nums)] = sorted(nums[i+1:len(nums)])
                return
               
            
        
        # nothing changed, revert
        nums.reverse()
        
```

solution2 find the first one that  breaks descending order.  
**that is to say, in soluton1, if you find one , it is always the one next to it**
```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                # find smallest
                win = i
                smallest = nums[i]
                for j in range(i+1,len(nums)):
                    if nums[j] > nums[i-1] and nums[j] < smallest:
                        win = j
                        smallest = nums[j]
                        
                nums[i-1],nums[win] = nums[win],nums[i-1]
                nums[i:len(nums)] = sorted(nums[i:len(nums)])
                return 
            
        # nothing changed, revert
        nums.reverse()
        
```