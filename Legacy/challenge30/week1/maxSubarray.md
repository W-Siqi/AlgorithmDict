# 经典题了
```py
# 初始值的设定，maxSum不能设为0，因为可能最大值为负数
# minSum必须设为0，它表示不减去任何前缀，就是本身
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minSum,accumSum,maxSum = 0,0,-float("inf")
        for n in nums:
            accumSum += n
            maxSum = max(maxSum,accumSum - minSum)
            minSum = min(minSum,accumSum)
        return maxSum
            
```

# divide&concer 解法
这个解法之前也写过。  
就是对于[left arr] mid [right]  
计算3个sum：
1. 一个是它本身的[left，right]的最大sum。
2. 最左边元素开始的最大sum
3. 最右边元素结尾的最大sum  
后面两个sum，是为了计算第一个sum准备的。  
因为sum。无非mid本身, mid 拼接左边,右边。 或者纯左边和右边。