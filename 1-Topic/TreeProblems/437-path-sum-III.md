# trick:累加和
有一个原题是，求连续sum为target。 用到的技巧，就是一直累加sum，配合hash可以做到O（N）
## 易错点1：但是一定要小心负数和0
累加和里面，如果出现负数，那么出现的sum是不唯一的。
## 易错点2： 别忘了先把0 push进去
就是序列本身就是sum的情况，需要set里面有个0保证这种情况也判定对
# wrong answer log.
直接生成root->leaf的path进行判断。  
这样不行，中间的子路径可会为count多次，所以只能在遍历到这个节点的时候，立马判定以这个节点为结尾的。

# 暴力解法怎么做？
以每个node作为起点，进行DFSpath。  
算法复杂度O(N*N)

# solution（非暴力，使用累加和）
```py
class Solution(object):
    def pathSum(self, root, sum):
        res = [0]
        def dfs(node,sums,pathsum):
            if not node: return
            
            # check
            pathsum += node.val
            if pathsum - sum in sums:
                res[0] += sums[pathsum - sum]
                
            # new prefix sums          
            newsums = collections.Counter(sums)
            newsums[pathsum]+=1
            
            # recursive
            dfs(node.left,newsums,pathsum)
            dfs(node.right,newsums,pathsum)
                
        initsums = collections.Counter()
        initsums[0] = 1
        dfs(root,initsums,0)
        return res[0]
```