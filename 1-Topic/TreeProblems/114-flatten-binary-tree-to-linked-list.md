# 描述递归操作
这题的精髓，在于你怎么递归地去描述fallten这个操作
# 描述1
flatten（root）：  
1. 我先把左子树摘了，并到right，保证root到right是flatten
2. 然后继续faltten(right)
```py
class Solution(object):
    def flatten(self, root):
        if not root or (not root.left and not root.right):
            return 
        
        if root.left:
            p = root.left
            while p.right:
                p = p.right
            p.right = root.right
            root.right = root.left
            root.left = None
        
        self.flatten(root.right)
```
# 描述2
flatten(root):  
1. flatten 左边
2. faltten 右边
3. flatten好了到左边拼到faltten好了的右边


```py
class Solution(object):
    def flatten(self, root):
        if not root: return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            tail = root.left
            while tail.right:
                tail = tail.right
            tail.right = root.right
            root.right = root.left
            root.left = None
```