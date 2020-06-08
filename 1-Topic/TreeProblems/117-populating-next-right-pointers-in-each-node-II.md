# 别忘了空间优化也可做文章
这题的时间优化基本是固定死的。  
但是空间优化上可以大做文章。  

这题可以做到，用O（1）的指针按图索骥遍历下去。  
感觉上有点像CG里halfedge mesh那种数据结构，就是通过额外指针，摸索连通到目标节点
```py
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def nextHasChild(node):
            p = node
            while p and not p.left and not p.right:
                p = p.next
            return p
        
        def leftMostChild(node):
            if node.left: return node.left
            else: return node.right
            
        start = root
        while start:
            cur = nextHasChild(start)
            if cur: start = leftMostChild(cur)
            else: start = None
 
            while cur: 
                nextVisit = nextHasChild(cur.next)
                if cur.left:
                    if cur.right: cur.left.next = cur.right
                    elif nextVisit: cur.left.next = leftMostChild(nextVisit)
                if cur.right and nextVisit:
                    cur.right.next = leftMostChild(nextVisit)
                # move to next
                cur = nextVisit
        return root
```