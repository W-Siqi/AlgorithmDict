# 【重点题】
# 排列组合情形与DP
这道题目仔细分析后，可以走两个流派，这两个都是很常见的排列组合情形。  
而且DP的方式很general，因此是很容易迁移的经典情形。
## 流派1： 把k的邮箱分配到h个坑里怎么配
首先很简单的证明，如果一个mailbox管1组house的话，放中间是最优。  
而放中间 == 放中间的house上，或者放在中间的那个区间上，而后者可以转化为放在这个区间的端点上。  
这样连续化为离散了，最优解总是会放在house上面  
## 流派2： h个member怎么分成k组
上面证明了最优策略后，其实分组这个思路是最直接的。 这是当时dp不熟没意识到分组这个模型dp很方便...
# solution1: dp[k][h] 第k个box放在第h房子的最优解
## dp[k][h]值代表啥
contest的最优解是只考虑前h个房子，这是为了方便状态转移。  
但一想想，直接考虑所有房子也方便，因为h靠后的跟谁比较近也只有两个候选者
## TLE 一个地方断路返回一下
最优有一个case超时了，但时间卡得很紧，不是数量级的超标。  
这个时候往往考虑一下剪枝，断路返回之类的。  
果然，我在更新状态的时候，有的状态是不存在的，比如前h个房子放的mailbox不可能超过h。  
这一点断路后，那个case的速度快了3倍
- **教训**：断路返回这种，应该是成为一种习惯，不要总是想当然的全遍历
```py
class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        houses.sort()
        dp = [[float("inf") for h in range(len(houses))]for m in range(k)]
        for m in range(len(dp)):
            for h in range(m,len(houses)):
                if m == 0:
                    dp[m][h] = 0
                    for preh in range(h):
                        dp[m][h]+=houses[h]-houses[preh]
                else:
                    for preh in range(h):
                        newcost = 0
                        for midh in range(preh+1,h):
                            newcost += min(houses[h]-houses[midh],houses[midh]-houses[preh])
                        dp[m][h] = min(dp[m][h],dp[m-1][preh]+newcost)
        res = float("inf")
        for h in range(len(houses)):
            cost = dp[k-1][h]
            for posth in range(h+1,len(houses)):
                cost += houses[posth]-houses[h]
            res = min(res,cost)
        #print(dp)
        return res
```

# solution 2 dp[k][h] 前h个房子分成k组的最优解
其实仔细想想，把一个区间divide成k个区间，这个情形应该是挺常见的。  
这个解就没自己写了：  
https://leetcode.com/problems/allocate-mailboxes/discuss/685620/JavaC%2B%2BPython-Top-down-DP-Prove-median-mailbox-O(n3)