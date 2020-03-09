# solution1: O(n^2)
```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float('inf')
        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s += nums[j]
                maxSum = max(maxSum,s)
        
        return  maxSum
```

# solution2: DP O(n)
```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [nums[0]]
        for i in range(1,len(nums)):
            dp.append(max(dp[i-1]+nums[i],nums[i]))
        
        res = dp[0]
        for s in dp:
            res = max(res,s)
            
        return res
```

# solution3: divide and conqure
```py
 class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def divc(nums,l,r):
            # analyze should be : [smax,lmax,rmax,allsum]
            if l > r:
                return [0,0,0,0]
            elif l == r:
                return  [nums[l],nums[l],nums[l],nums[l]]
            
            mid = (l+r)//2
            resl = divc(nums,l,mid)
            resr = divc(nums,mid+1,r)
            
            lmax = max(resl[1],resl[3]+resr[1])
            rmax = max(resr[2],resl[2]+resr[3])
            smax = max(resl[2]+resr[1],resl[0],resr[0],lmax,rmax)
            allsum = resl[3]+resr[3] 
            return [smax,lmax,rmax,allsum] 
        
        res = divc(nums,0,len(nums)-1)
        return res[0]
```