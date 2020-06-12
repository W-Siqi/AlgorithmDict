# 寻找最优subarray
理论上这种找最优解的，for循环里面，你每次动一下end或start，都需要尝试更新一下result。 总之就是别漏掉
# solution
```py
class Solution(object):
    def longestOnes(self, A, K):
        zeros = collections.deque()
        start = res = 0
        for end in range(len(A)):
            if A[end] == 0:
                zeros.append(end)
                
            if len(zeros) > K:
                start = zeros[0]+1
                zeros.popleft()
            res = max(res,end-start+1)
        return res
```