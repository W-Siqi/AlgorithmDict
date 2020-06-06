# DP的实质
这题是个很生动的例子，揭示了DP，DFS，bottom-up 之间的联系
## 一个wrong answer：
利用最优子结构的naive解法，是遍历，而不是直接挑选。 直接挑选是能证明，那个子结构一定是最优的。  
这里，就是如果parent不选，那么child是选最优的，而“child被选择”不代表是最优的（下意识直觉认为他一定是最优的了），需要两种情况max一下
# solution
```py
class Solution(object):
    def rob(self, root):
        def dp(node):
            if not node: return (0,0)
            lyes,lno = dp(node.left)
            ryes,rno = dp(node.right)
            return (node.val+lno+rno,max(lno,lyes)+max(rno,ryes))
        
        v1,v2 = dp(root)
        return max(v1,v2)
        
```