# solution 1
递归，三四行就写完的东西。这里主要讨论下非递归
# solution 2
CG的实验一写，发现非递归的写法是有实际作用的。  
实际上，中序遍历（DFS最常见的）的非递归写法是超级简单的。
```py
class Solution(object):
    def invertTree(self, root):
        stack = [root]
        
        while stack:
            top = stack.pop()
            if not top: continue
            top.left,top.right = top.right,top.left
            stack.append(top.right)
            stack.append(top.left)
            
        return root
```