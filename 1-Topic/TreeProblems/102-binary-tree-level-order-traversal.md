# DFS vs BFS
这题最直观的就是BFS，
但**传递depth的DFS很多时候是BFS的替代。**  

实际测出来还是DFS更快，也许和环境，testcases有关，但DFS写法比BFS更简洁是一定的！
```py
class Solution(object):
    def levelOrder(self, root):
        def dfs(levels,root,depth):
            if not root: return 
            levels[depth].append(root.val)
            dfs(levels,root.left,depth+1)
            dfs(levels,root.right,depth+1)
            
        levels = collections.defaultdict(list)
        dfs(levels,root,0)
        res = [levels[i] for i in range(len(levels))]
        return res
```