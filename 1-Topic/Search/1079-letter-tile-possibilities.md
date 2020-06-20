# 排列组合 - 排列问题
和组合问题不一样，排列问题做决策的时候，当前的选项和之前的步骤相关的。  
换句话说，**要逐步传递做选择的上下文**
## DFS 与 Backtraking
有的理解是，带上下文传递的DFS搜索就是回溯法backtracking  
在我的理解里，backtracking算是DFS的一种形式，只是可能描述过程的角度不一样。  
而实现方式上，就是上下文传引用，函数调用完了要回溯上下文。工程的角度上，这里省去了内存拷贝的开销。   
（像这里，直接拷贝比回溯速度差2倍！）
# solution 
```py
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        self.res = 0
        def dfs(cnt):
            for key in cnt.keys():
                self.res += 1                
                cnt[key] -= 1
                if cnt[key] == 0:
                    del cnt[key]                
                dfs(cnt)                
                cnt[key] += 1
        dfs(collections.Counter(tiles)) 
        return self.res
            
        
```