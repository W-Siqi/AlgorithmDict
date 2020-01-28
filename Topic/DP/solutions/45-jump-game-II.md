# solution1: normal dp
but, think about the worest case:
[99999,999999,999999,999999,....999999] 
```py
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0
        
        dp = [len(nums)]*len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            # dp previrous
            for j in range(i+1,min(len(nums),i+nums[i]+1)):
                dp[i] = min(dp[i],1+dp[j])
        
        return dp[0]
```
# solution2: gready & shortest path
alway try to get the largest part.  
or we can treat it as shortest path in a map, we use BFS.
```py
# think about the wors
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        preReach = 0
        reach = nums[0]
        step = 1
        while reach < len(nums)-1:
            nextReach = reach
            for i in range(preReach+1,reach+1):
                nextReach = max(nextReach,i+nums[i])
            
            preReach = reach
            reach = nextReach
            step += 1
        return step
```