# 标记node
这题最初写法很复杂，用了两个递归，思路混乱。  
核心原因是这样的：  
- 我遍历到某个节点，不知道要不要把这个node添加到result上去，因为无法判断是不是root。  
- 然后我就很蠢的用两个不同的递归函数区分开来，一个专门负责添加root，另一个专门负责删节点...
## 但其实用flag标记一下，就可把两个递归做的事情合二为一

# solution1 双递归版
极其复杂，而且两个递归还需要用一个queue沟通
```py
class Solution(object):
    def delNodes(self, root, to_delete):
        self.res = []
        stack = [root]
        
        def dfsDel(node):
            if not node: return 

            if node.left and node.left.val in to_delete:
                stack.append(node.left.left)
                stack.append(node.left.right)
                node.left = None
            else:
                dfsDel(node.left)
                
            if node.right and node.right.val in to_delete:
                stack.append(node.right.left)
                stack.append(node.right.right)
                node.right = None
            else:
                dfsDel(node.right)
            
                
                    
        def buildFori(node):
            if not node: return 
            if node.val in to_delete:
                stack.append(node.left)
                stack.append(node.right)
            else:
                self.res.append(node)
                dfsDel(node)
                
        while stack:
            top = stack.pop()
            buildFori(top)
        return self.res
```
# solution2 合并版
```py
class Solution(object):
    def delNodes(self, root, to_delete):
        self.res = []
                    
        def buildFori(node,isRoot):
            if not node: return 
            if node.val in to_delete:
                buildFori(node.left,True)
                buildFori(node.right,True)
                return 
            
            if isRoot:
                self.res.append(node)
            
            if node.left and node.left.val in to_delete:
                buildFori(node.left,True)
                node.left = None
            else:
                buildFori(node.left,False)
                
            if node.right and node.right.val in to_delete:
                buildFori(node.right,True)
                node.right = None
            else:
                buildFori(node.right,False)
                
        buildFori(root,True)
        return self.res
```
# solution 2 简化逻辑
这题节点有没delete，我在两个地方判断了：  
1. 自己有没有被delete，否则要给两个child递归调用
2. child有没有被delete，否者指针要设成None
## 还是那个原则：要知道child怎么怎么了，可以通过返回值bottom-up  
这样代码就可简化：
```py
class Solution(object):
    def delNodes(self, root, to_delete):
        self.res = []
                    
        def buildFori(node,isRoot):
            if not node: 
                return None
            
            isDel = node.val in to_delete
                
            if isRoot and not isDel:
                self.res.append(node)
             
            node.left = buildFori(node.left,isDel)
            node.right = buildFori(node.right,isDel)
            return None if isDel else node

        buildFori(root,True)
        return self.res
```