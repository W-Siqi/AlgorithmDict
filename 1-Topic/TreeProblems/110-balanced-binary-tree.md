# 同100，tree的recursive defination
```py
class Solution(object):
    def isBalanced(self, root):
        # return:(bool,depth)
        def dfs(root):
            if not root: return (True,0)
            lbal,ldep = dfs(root.left)
            rbal,rdep = dfs(root.right)
            return (lbal and rbal and abs(ldep-rdep) <= 1,max(ldep,rdep)+1)
        
        isbal,depth = dfs(root)
        return isbal
```