# 排列组合 - combination
按照step进行dfs搜索就行了，每个step决定这个number是选0,1,2，3...个。   
# solution 1 DFS
## 一个wrong answer
我这题满足target之后没有立马return，导致了duplication出现。  
因为比如index为3的时候满足了，index4选0个，index5选0个也算了进去...  
这个bug和path sumIII 的一种写法很像，忘了树的公共前缀被重复计算了很多次
```py
class Solution(object):
    def combinationSum2(self, candidates, target):
        items = collections.Counter(candidates).items()
        res = []
        def dfs(index,target,path):
            if target == 0:
                res.append(path)
                return
            if index >= len(items):
                return        
            num,count = items[index]
            for i in range(count+1):
                if target - i*num < 0:
                    break
                dfs(index+1,target-i*num,path+[num]*i)
            
        if candidates:
            dfs(0,target,[])
        return res
```
# solution 2 DP
这题用DP解没尝到什么好处。  
因为很明显的一个维度就是target，而target有多大是不清楚的,万一来个21亿呢？  
另一个是，这题还是有点类似枚举，dp存的不是最优解的那个值，而是整个序列...
```py
class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        dp = [[[]]] + [[] for i in range(target)]
        for i in range(1, target + 1):
            for number in candidates:
                if number > i: break
                for L in dp[i - number]:
                    if not L or number >= L[-1]: dp[i] += L + [number],
        return dp[target]
```