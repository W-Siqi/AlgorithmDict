# solution 1  (cache pre&suf)
runtime O(n) , space O(n)
```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        preSum = []
        sufSum = [0]*len(nums)
       
        sumP = 1
        for num in nums:
            sumP *= num
            preSum.append(sumP)
            
        sumP = 1
        for i in range(len(nums)-1,-1,-1):
            sumP *= nums[i]
            sufSum[i] = sumP
            
        output = [0]*len(nums)
        for i in range(1,len(nums)-1):
            output[i] = preSum[i-1] * Sum[i+1]
        
        if len(nums) > 1:
            output[0] = sufSum[1]
            output[-1] = preSum[-2]
            
        return output
```

# solution 2 
runtime O(n), space O(1)
```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        output = [1]*len(nums)
       
        sumP = 1
        for i in range(len(nums)-1):
            sumP *= nums[i]
            output[i+1] *= sumP
            
        sumP = 1
        for i in range(len(nums)-1, 0,-1):
            sumP *= nums[i]
            output[i-1] *= sumP
            
        return output
```