# main
1. 这题还是bool式的二分。  
2. 但是greedy+BS这套连招真的漂亮，是有参考价值的。    
很多时候greedy的边界是个变量，而这个变量，我们可以去暴力尝试，而这里，暴力尝试化为了二分搜索

# 【填坑】
用DP的解法

# solution
```py
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isPossible(nums,m,maxSum):
            curSum,curCount = 0,1
            for n in nums:
                if n > maxSum:
                    return False
                if curSum + n > maxSum:
                    curCount += 1
                    curSum = n
                else:
                    curSum += n
            
            return curCount <= m
        
        lo,hi = 0,sum(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if isPossible(nums,m,mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```