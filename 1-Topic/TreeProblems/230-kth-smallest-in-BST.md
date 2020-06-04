# BST转list
```py
class Solution(object):
    def kthSmallest(self, root, k):
        res = [0]
        count = [0]
        def dfs(node,k):
            if not node: return        
            dfs(node.left,k)            
            count[0] += 1            
            if count[0] == k: res[0] = node.val
            elif count[0] > k:return
            elif count[0] < k: dfs(node.right,k)
            
        dfs(root,k)
        return res[0]           
```