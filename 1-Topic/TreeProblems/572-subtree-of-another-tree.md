
# wrong solution 
出发点是：我是你的subtree,要么我是就是你本身，要么我是你child的subtree。  
但是，一旦走“我是你本身”这个分支，后面的child就是需要严格相等了，不能继续递归subtree了
```py
class Solution(object):
    def isSubtree(self, s, t):
        if not s and not t: return True
        elif not s or not t: return False
        
        if self.isSubtree(s.left,t): return True
        elif self.isSubtree(s.right,t):return True
        elif s.val == t.val and self.isSubtree(s.left,t.left) and self.isSubtree(s.right,t.right):return True
        
        return False
```
# solution 1
其实就是遍历节点，看一下这个tree和那个tree是不是一样的
```py
class Solution(object):
    def isSubtree(self, s, t):
        def isSame(a,b):
            if not a and not b: return True
            elif not a or not b: return False
            else: return a.val == b.val and isSame(a.left,b.left) and isSame(a.right,b.right)
        
        if not s: return not t
        return isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)     
```

# solution2 奇淫技巧
基本思想是，如果一个tree是另一个的subtree。  
那么他的遍历序列也是另一个的sublist。  
**BUT**！这个遍历序列，是需要标识空child，以及是左child还是右child。  
（因为仅凭一个中序或前序，我们是无法构建二叉树的，因为他不能唯一确定一个二叉树）  