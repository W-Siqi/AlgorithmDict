# DFS 
这题除了要考虑，你追踪的信息是什么之外，就是个最普通的DFS  
1. 最粗暴，追踪path
2. 用hash追踪数字出现次数（因为要回文，奇数次最多1次）
3. 用set追踪当前为奇数次的数字（类似于括号算法，新加入会抵消）


当时用的是set，但因为数字是1-9，用hash也是很快的：  
**Q：python的set的实现方式是？**  
A： set和dict实现方式都是hash表！ （所以我用set也是很快的~）
```py
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        def countPath(root,curSingle):
            if not root:  return 0
            
            if root.val in curSingle: curSingle.discard(root.val)
            else: curSingle.add(root.val)
                
            if root.left == None and root.right == None:
                if len(curSingle) <= 1:
                    return 1
                else:
                    return 0
            else:
                return countPath(root.left,curSingle.copy())+countPath(root.right,curSingle.copy())
        
        s = set()
        return countPath(root,s)
'''