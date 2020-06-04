# BST
同95
# why这题不能用DP？
**不满足DP中的“重复子结构计算”这一先决条件，枚举的时候，同样是dp[i]，是不一样的。**  
95是数数字,dp[i]是个数，和状态推导无关，而这题是要把具体的sub tree都枚举出来。  

```py
class Solution(object):
    def generateTrees(self, n):
        def trees(n,base):
            if n == 0:
                return [None]
            
            res = []
            for i in range(1,n+1):
                lefts = trees(i-1,base)
                rights = trees(n-i,base+i)
                for l in lefts:
                    for r in rights:
                        res.append(TreeNode(i+base,l,r))
            return res
        
        if n == 0:
            return []
        return trees(n,0)
```