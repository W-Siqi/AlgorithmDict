# 小技巧here
我最初的写法，是传递当前sum和target（更蠢的传递path的list）  
但其实只要传remain，即与目标的差就ok了
# solution1
```py
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root: return False
        
        newSum = sum - root.val
        if not root.left and not root.right:
            return newSum == 0
        else: return self.hasPathSum(root.left,newSum) or self.hasPathSum(root.right,newSum)
```
# solution 2 牵强的BFS解法
正常的BFS写法，有个缺点就是无法传参，如果queue里面只存val的话。  
但是你一定要传参，比如这里的remain，也不是不可以，那么queue里面其实存的就是'栈帧'了
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root: return False
        
        queue = [(root,sum-root.val)]
        while queue:
            top = queue.pop(0)
            if not top[0].left and not top[0].right:
                if top[1] == 0:
                    return True
            if top[0].left:
                queue.append((top[0].left,top[1]-top[0].left.val))
            if top[0].right:
                queue.append((top[0].right,top[1]-top[0].right.val))
        return False
```