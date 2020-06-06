# 同199和102,思路一模一样
```py
class Solution(object):
    def largestValues(self, root):
        levelmax = {}
        def dfs(node,depth):
            if not node: return 
            if depth not in levelmax or levelmax[depth] < node.val:
                levelmax[depth] = node.val
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return [levelmax[i] for i in range(len(levelmax))]
```