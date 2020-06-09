# 最低共同祖先
要避免暴力，就需要观察出一个现象：  
如果左右子树的有一个完全没有那个target节点，那么就在另一个子树上。  
这里的体现就是：
1. 左右子树出现高度不一，那么就是高的那个。  
2. 如果高度一样，那么就是自己，或者parent。
# 写法上优化，没必要的two pass
我的第一个有点蠢，因为父节点要知道子节点的“depth”才能判断，就直接先one pass把所有节点的depth都先算出来...  
然而:  

父节点要知道子节点信息--> bottom up返回值传递。  
one pass搞定
# solution (two pass)
```py
class Solution(object):
    def lcaDeepestLeaves(self, root):
        self.res = None
        def depth(node):
            if not node: return 0
            dep = max(depth(node.left),depth(node.right)) + 1
            node.depth = dep
            return dep
        
        def find(node):
            if not node: return 
            
            if not node.left and not node.right:
                self.res = node
                return 
            
            if not node.left:
                find(node.right)
                return 
            if not node.right:
                find(node.left)
                return 
                
            if node.left.depth == node.right.depth:
                self.res = node
            elif node.left.depth > node.right.depth:
                find(node.left)
            else:
                find(node.right)
                
        depth(root)
        find(root)
        return self.res      
```

# solution 2 (one pass)
```py
    def lcaDeepestLeaves(self, root):
        def helper(root):
            if not root: return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            return h1 + 1, root
        return helper(root)[1]
```