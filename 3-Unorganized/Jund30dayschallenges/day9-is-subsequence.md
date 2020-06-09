# Greedy VS. DP
这题我第一反应，是DP。因为可以递归描述，然后dfs。  
后来发现，DFS的时候，“不存在分支”，因为如果尽早遇见目标，最优解也一定是最优匹配掉。  
这意味着，可以直接greedy
## 很多时候，DP的时候，发现max里面的是可以直接定下最优解了，那么意味着贪心可能就来了
```py
class Solution(object):
    def isSubsequence(self, s, t):
        dic = collections.defaultdict(list)
        for i,c in enumerate(t):
            dic[c].append(i)

        index = -1
        for c in s:
            if c not in dic:
                return False
            found = False
            for i in dic[c]:
                if i > index:
                    index = i
                    found = True
                    break
            if not found:
                return False
        return True          
```