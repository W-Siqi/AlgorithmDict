# solution
corner case: 0!!!   
```py
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(len(nums) -1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        
        for start in range(len(nums)-1):
            subSum = nums[start]
            for end in range(start+1,len(nums)):
                subSum += nums[end]
                if subSum%k == 0:
                    return True
                
        return False
```