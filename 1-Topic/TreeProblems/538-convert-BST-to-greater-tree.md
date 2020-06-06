# 还是BST的那个特性：中序遍历即顺序
知道这个事实，代码就很简单，跑一遍遍历就ok了
```py
class Solution(object):
    def convertBST(self, root):
        s = [0] 
        def dfs(root):
            if not root: return 
            dfs(root.right)
            root.val = s[0] = root.val + s[0]
            dfs(root.left)            
        dfs(root)
        return root
```