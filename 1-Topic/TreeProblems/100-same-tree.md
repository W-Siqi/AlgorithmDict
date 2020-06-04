# 简洁写法
p,q 为不为None有4种情况。  
但是这里的if/else只写了3种分支，  
因为只有1个位None，都是返回True，没区别。所以不用写if (q and not p) or (not q and p) 这种恶心的写法。  

**任何简化if/else的方式，前提是对所有cases一清二楚！**
```py
class Solution(object):
    def isSameTree(self, p, q):      
        if q and p and q.val == p.val and self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right): return True
        elif not p and not q: return True
        else: return False
```