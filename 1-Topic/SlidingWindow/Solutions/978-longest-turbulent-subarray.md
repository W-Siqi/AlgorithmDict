# 寻找最优subarray
这题之所以可以DP，首先它是一个寻找最优的问题，其次，最优的比较只需要依赖最后一次波动，而不是之前所有的值
# solution 1 sliding window
```py
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        preSign = 0
        res = 1
        start = 0
        for end in range(1,len(A)):
            curSign = ""
            if A[end] > A[end-1]: curSign = "up"
            elif A[end] < A[end-1]:curSign = "down"
            else: curSign = "eql"
            
            valid = (preSign is "" and curSign is not "eql") or(preSign is "up" and curSign is "down") or (preSign is "down" and curSign is "up")
            #print(A[end],valid)
            if valid: 
                res = max(end-start+1,res)
            else:
                start = end -1
            preSign = curSign
            
        return res
        
```
# solution 2 DP