# design： 考虑极端情形
这题brute force看似是没有问题的。  
但是树的深度很深（极端例子就是很长的链表），每次访问都是O（N）的复杂度   

## 通用情形抽象
这题的jump array，很少额外空间，实现了树 lgN的随机访问。  
Q：为什么链表没出现过这问题？  
A: 因为链表直接存array都行啊...而树不可以，树是有重叠的链表，转成array会炸掉。
# 缓存结果
## 缓存depth
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

## 缓存parents
应对最主要的，树的形状很变态，深度很深的那种。  
你不能把path全缓存成array，duplication会让space直接爆炸。  

这一1个解就是按照二分的步长缓存parent。  
这样回溯前面可以做到lgN，而存储容量也N*lgN大大减少。
https://leetcode.com/problems/kth-ancestor-of-a-tree-node/discuss/686362/Python-Jump-Parent