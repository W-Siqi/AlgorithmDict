# solution 1 - 组合问题，挑选定长
```py
class Solution(object):
    def combine(self, n, k):
        res = []
        def dfs(i,comb):
            if len(comb) == k:
                res.append(comb)
                return 
            if i > n:
                return 
            dfs(i+1,list(comb))
            dfs(i+1,comb+[i])
        
        dfs(1,[])
        return res
```
# solution2 - “排列问题”，去除重复
```py
class Solution(object):
    def combine(self, n, k):
        res = []
        def dfs(comb):
            if len(comb) == k:
                res.append(comb)
                return 
            start = 0 if not comb else comb[-1]
            if start == n:
                return 
            else:
                for num in range(start+1,n+1):
                    dfs(comb+[num])
        dfs([])
        return res
```
# solution3 - (solution2+剪枝)
速度将近快了10倍！  
所以啊..DFS的剪枝有时候是很恐怖的！
```py
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(comb):
            if len(comb) == k:
                res.append(comb)
                return 
            start = 0 if not comb else comb[-1]
            if start == n:
                return 
            else:
                # 剪枝，数字太大了不行，就算后面+1,+1都撑不到k长度的
                for num in range(start+1,n+len(comb)-k+2):
                    dfs(comb+[num])
        dfs([])
        return res
```