# motivation
这里hash的另一个动机，就是“对号入座”来达到点名、统计的目的  

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