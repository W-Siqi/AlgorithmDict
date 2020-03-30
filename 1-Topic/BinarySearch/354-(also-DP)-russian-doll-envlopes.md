# key&tag
其实就是一个LIS（longest increasing subsequence）问题  
所以第一步是问题的转化  
其次，naive的LIS是O(n^2)，但是可以用BS进行优化。  
这里BS的动机，最小tail 和 len是正相关的
## wrong answer
凡是依赖sort的，一定考虑duplication问题！
这里envilopes 的wid 是可能重复！ 这样就不能直接对height 用LIS
## lambda排序的进阶key
  第一个key一样，就按第二个k
```py
envelopes.sort(key = lambda x:(x[0],-x[1]))
```

# solution
```py

# 这里BS的动机，最小tail 和 len是正相关的
# BS找最大不超过的写法关注一下，
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        # 双lambda？？
        envelopes.sort(key = lambda x:(x[0],-x[1]))
        tails = [float("inf")]*len(envelopes)
        maxL = 1
        for i in range(len(envelopes)):
            # find max lower in tails
            lo,hi = 0,len(envelopes)-1
            while lo <= hi:
                mid = (lo+hi)//2
                if tails[mid] < envelopes[i][1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            if hi == -1:
                tails[0] = min(envelopes[i][1],tails[0])
            else:
                tails[hi+1] = min(envelopes[i][1],tails[hi+1])
                maxL = max(maxL,hi+2)            
        return maxL
```