# takeaway - O(n)下的优化思路
按理来说，O(n)后面是O(lgn),再后面是O(1).  
但是这种跨越往往意味着换算法，是本质上的改变。  
但是O(n)到O(lgn)之间，还有一个进步空间：
- 剪枝
- 快速中断&排除  
在有的情形下，还是会有几倍的优化（虽然比不上几何倍数的跨越...）
# solution 0 - probably最优解
## 基于后面的“中序遍历”做的快速中断
虽然还是O(n),但实际是O(k),k是第一个不对劲的地方就可以返回了    
当然，再快一点，就做系统上的优化：改成非递归
```py
class Solution(object):
    def isValidBST(self, root):
        self.res = True
        self.seq = []
        def sequence(root):
            if not root: return 
            sequence(root.left)
            if self.seq and root.val <= self.seq[-1]: 
                self.res = False
            else:
                self.seq.append(root.val)
                sequence(root.right)
        
        sequence(root)
        return self.res
```

# solution 1 tree的递归定义
```py
class Solution(object):
    def isValidBST(self, root):
        # return (valie,min,max)
        def valid(root):
            if not root:
                return (True,float("inf"),-float("inf"))
            lv,lmin,lmax = valid(root.left)
            rv,rmin,rmax = valid(root.right)
            
            if not lv or not rv or root.val <= lmax or root.val >= rmin: return (False,0,0)
            
            return (True,min(root.val,lmin,rmin),max(root.val,lmax,rmax))
        res,minv,maxv = valid(root)
        return res
```
# solution 2 BST转list
实现方法有两种，算法复杂度是一样的。  
但是因为数据结构的开销，时间效率几乎是两倍（一个beat99%，一个beat12%）
## approach 1 递归构造，分治
这个缺点，就是用list[]拼接的话，会有频繁的数据拷贝，所以会很慢
```py
class Solution(object):
    def isValidBST(self, root):
        def sequence(root):
            if not root: return []
            else: return sequence(root.left)+[root.val]+sequence(root.right)
        
        seq = sequence(root)
        res = True
        for i in range(len(seq)):
            if i + 1 < len(seq) and seq[i] >= seq[i+1]: 
                res = False
                break
        return res
```

## approach 2 中序遍历
```py
class Solution(object):
    def isValidBST(self, root):
        self.seq = []

        def sequence(root):
            if not root: return 
            sequence(root.left)
            self.seq.append(root.val)
            sequence(root.right)
        
        sequence(root)
        seq = self.seq
        res = True
        for i in range(len(seq)):
            if i + 1 < len(seq) and seq[i] >= seq[i+1]: 
                res = False
                break
        return res
            
```
# solution 3
root作为左边的上界，右边的下界，一层层传递过去
```py
class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))
```