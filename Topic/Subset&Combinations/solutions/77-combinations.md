# find combinations with constraint
the constrant is the length
```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(n,k,0,[],res)
        return res
    
    def dfs(self, n,k,cur,path,res):
        if len(path) == k:
            res.append(path)
            return
        
        for i in range(cur + 1, n+1):
            self.dfs(n,k,i,path + [i],res)
```