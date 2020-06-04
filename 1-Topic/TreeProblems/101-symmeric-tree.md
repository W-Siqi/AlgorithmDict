这题倒是没看出来章法。  
靠观察和经验上的直觉了。
```py
class Solution(object):
    def isSymmetric(self, root):
        def sym(left,right):
            if left and right:
                return left.val == right.val and sym(left.left,right.right)and sym(left.right,right.left)
            
            if left == right: return True
            else: return False
            
        return sym(root,root)
```