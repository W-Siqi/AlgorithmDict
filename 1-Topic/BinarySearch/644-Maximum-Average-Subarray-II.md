# main
这题非常tricky。  
首先要知道 累加sum 的技巧，这个来求连续最大和是O(n)的。  
而对于给定的avergae，我们可以他转化accumulate sum。  
然后二分去尝试策略。

# solution:
有漏过edge case，在注释
```py
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:    
        def check(nums,k,avg):
            sums = []
            curSum = 0
            for i in range(k):
                curSum += (nums[i]-avg)
                sums.append(curSum)
            if curSum >= 0:
                return True
            
            preMinSum = 0 # 【edge case】初始化为nums[0]!, 漏掉了不减去的情况！！！！！
            for i in range(k,len(nums)):
                preMinSum = min(sums[i-k],preMinSum)
                curSum += (nums[i]-avg)
                sums.append(curSum)
                if curSum - preMinSum >= 0:
                    return True
            return False
        
        lo,hi=min(nums),max(nums)
        while  hi - lo > 10**-5:
            mid = (lo+hi)/2
            if check(nums,k,mid):
                lo = mid + 10**-5
            else: 
                hi = mid
        
        return lo

```