# why这个subarray问题里，sliding window 行不通
这题不能用sliding window，因为当上一轮无法继承到下一轮上。  
如果第一个前缀改了，因为要保证顺序，后面的都要全部重新核算。  
其他的情况是，下一轮可以继承上一轮的结果快速重置start指针。

# DP
subarray这个课题，dp也是经常出现。  
因为subarray，本身就是个天然的子问题。
# solution (TLE)
O(S*T*lgS)  
这题把dp[i][j] 的j状态定义为S和j匹配的时候。  
但是，定义为问题规模，那么就可以过了。
```py
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        charIndex = collections.defaultdict(list)
        for i,char in enumerate(S):
            charIndex[char].append(i)
        dp = [[float("inf") for j in range(len(S))] for i in range(len(T))]
       
        for i in range(len(T)):
            for j in range(len(S)):
                if T[i] != S[j]:
                    continue
                    
                if i == 0:
                    dp[i][j] = 1
                    continue
                    
                indices = charIndex[T[i-1]]
                lo,hi = 0,len(indices)
                while lo < hi:
                    mid = (lo+hi)//2
                    if indices[mid] < j:
                        lo = mid+1
                    else:
                        hi = mid

                for index in range(lo-1,-1,-1):
                    k = indices[lo-1]
                    if dp[i-1][k] != float("inf"):
                        dp[i][j] = dp[i-1][k] + j - k
                        break

        minLen = float("inf")
        finalJ = 0
        for j in charIndex[T[-1]]:
            if dp[len(T)-1][j] < minLen:
                minLen = dp[len(T)-1][j]
                finalJ = j
        if minLen != float("inf"):
            return S[finalJ+1-int(minLen):finalJ+1]
        else:
            return ""
```