# tag: dp, subsequnce
# solution 1 (DP)
```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]: the max len of sub array end at nums[i]
        dp = [1]*len(nums)
        res = 0
        for i in range(len(nums)):
            # try to find previous subsequence
            for j in range(i):
                # check if nums[j] -> nums[i] can form subsequence
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
            res = max(res,dp[i])
        return res
```

# solution 2： anothor 'DP'
```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # best[i]: store the smallest tail value of , with length i
        best = [float("inf")]*(len(nums)+1)
        best[0] = -float("inf")
        for num in nums:
            for i in range(len(best)):
                if num > best[i]:
                    best[i+1] = min(best[i+1],num)
           
        for i,b in enumerate(best):
            if b == float("inf"):
                return i-1
        
        return len(best)-1
```

# soluton 3: optimize soluton 2 with binary search
```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # best[i]: store the smallest tail value of , with length i
        best = [float("inf")]*(len(nums)+1)
        best[0] = -float("inf")
        for num in nums:
            # find the biggest target while target < num
            lo, hi = 0,len(best) - 1
            while lo < hi:
                mid  = (lo + hi + 1) // 2
                if num < best[mid]:
                    hi = mid - 1
                else:
                    lo = mid
            if best[lo] == num:
                lo -= 1
            best[lo+1] = min(best[lo+1],num)
            
        for i,b in enumerate(best):
            if b == float("inf"):
                return i-1
        
        return len(best)-1
```
