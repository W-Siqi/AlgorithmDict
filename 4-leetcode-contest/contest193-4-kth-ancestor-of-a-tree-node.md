# design： 考虑极端情形
这题brute force看似是没有问题的。  
但是树的深度很深（极端例子就是很长的链表），每次访问都是O（N）的复杂度   
# 缓存结果
## solution1 缓存depth
这是我遇到一个case，出现大量的depth超范围的访问。    
(这个case是过了，但是其他case TLE)
```py
class TreeAncestor(object):

    def __init__(self, n, parent):
        self.n = n
        self.parent = parent
        self.depth = [-1]*len(parent)
        
        self.depth[0] = 0
        def filldepth(n):
            depth = self.depth
            path = [n]
            while depth[path[-1]] < 0:
                path.append(parent[n])
                
            for i in range(len(path)):
                depth[path[i]] = depth[path[-1]] + len(path) - i - 1

        for i in range(len(parent)):
            if self.depth[i] < 0:
                filldepth(i)

    def getKthAncestor(self, node, k):
        layers = self.layers
        if k >  self.depth[node]:
            return -1

        cur = node
        while k > 0 and cur >= 0:
            cur = self.parent[cur]
            k-=1

        if k == 0 and cur >= 0:
            return cur
        else:
            return -1
```

## naive方案
