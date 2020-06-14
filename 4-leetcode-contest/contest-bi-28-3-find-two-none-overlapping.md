# 【重点题】
# hash/perfix-sum/区间
求sum为target的区间，前用累加和O(N)整理出来。  
然后按照长度进行遍历。  

# solution 1 区间操作O（N*sqrt(N)）
这是一个比较直观的方法，直接把区间全部整理出来
## 这里的贪心法：pay attention to 区间两边的极值
最初的做法会超时，每个区间比过去很麻烦。  
但是对于2个数量级的，只要各自最左和最右的不overlap就可以了。  

```py
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        subs = collections.defaultdict(list)
        sums = {0:-1}
        cursum = 0
        for i,a in enumerate(arr):
            cursum += a
            if cursum - target in sums:
                start = sums[cursum-target] + 1
                subs[i-start+1].append((start,i))
            sums[cursum] = i
        lens = sorted(subs.keys())
        
        res = float("inf")
        for i in range(len(lens)):
            subleni =  subs[lens[i]]
            # match len[i] and len[i]
            if len(subleni) > 1 and subleni[0][1] < subleni[-1][0]:
                res = min(res,2*lens[i])
                continue
                
            # match len[i] with bigger
            for j in range(i+1,len(lens)):
                if subleni[0][1] < subs[lens[j]][-1][0] or subs[lens[j]][0][1] < subleni[-1][0]:
                    res = min(res,lens[j]+lens[i])
                    break
              
        # print(subs)
        if res == float("inf"): return -1
        else: return res
```

# solution 2 缓存最优解 O（N）
这里的一个转化就是，找[a,b]不overlap的，就是就是找到a为止最短的区间，或者从b开始的最短区间。  
无论是“到a为止的最优解”还是“从b开始的最优解”，都可以随着遍历max来逐步更新。
```py
class Solution(object):
    def minSumOfLengths(self, arr, target):
        presum = {0:-1}
        best = [float("inf")]*len(arr)
        cursum = 0
        res = curbest = float("inf")
        for i,a in enumerate(arr):
            cursum += a
            if cursum - target in presum:
                prei = presum[cursum-target]
                rangelen = i-prei
                curbest = min(curbest,rangelen)
                if prei >= 0:
                    res = min(res,rangelen+best[prei])       
            best[i] = curbest             
            presum[cursum] = i
            
        return res if res != float("inf") else -1
```