# DP
## 排列组合避免重复
做数学题的时候，避免2,1 和1,2 重复的方法，就是排序。  
所以这题看似只有1个维度dp[i]，i代表amount。   
但是这样会出现重复，为了避免重复，进行排序，  需要dp[i][j] ，j为只考虑前j个coins。
## 证明：不会出现引用未更新完的子结构
我在写 dp[i][j] += dp[i][j-1]的时候，怀疑这个时候dp[i][j-1]有没有更新完？  
实际上：
1. 下标遍历顺序是bottom up的
2. 每次更新都是完备的
那么就不存在更新了一半的子结构，因为每次引用的都是完备的，这一步就是完备的结构，给后面使用的也是完备的结果
```py
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0 for j in range(len(coins)+1)] for i in range(amount+1)]
        for c in range(len(coins)+1):
            dp[0][c] = 1
            
        for i in range(1,amount+1):
            for j in range(1,len(coins)+1):
                dp[i][j] += dp[i][j-1]
                count = 1
                while i - count*coins[j-1] >= 0:
                    dp[i][j] += dp[i - count*coins[j-1]][j-1]
                    count+=1
        print dp
        return dp[-1][-1]
```