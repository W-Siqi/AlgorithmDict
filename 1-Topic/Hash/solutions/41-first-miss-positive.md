because we just check if 1,2,3....n is in the array.  
to optimize repeating search, we use hash!
```py
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        hsh = [False]*(len(nums) + 1)
        for num in nums:
            if 1<= num <= len(nums):
                hsh[num] = True
        
        for i in range(1,len(nums)+1):
            if hsh[i] == False:
                return i
        
        return len(nums)+1
```