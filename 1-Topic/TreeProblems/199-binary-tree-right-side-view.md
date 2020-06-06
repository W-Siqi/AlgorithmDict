# DFS去替代BFS
这题和“102”很类似，
用带depth的DFS去替代BFS。  
除了实现简单，而是空间复杂度大多数情况更好。   
### 一个FACT：
dfs中，每一层node的遍历顺序，是有规律的，要么从左到右，要么从右到左。取决于遍历child是左边还是右边
```py
class Solution(object):
    def rightSideView(self, root):
        sides = collections.defaultdict(int)
        def dfs(node,depth):
            if not node:return
            sides[depth] = node.val
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return [sides[i] for i in range(len(sides))]
```