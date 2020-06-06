# 这里的逻辑简化
前后两个solution，第一步都是一样。统计所有subtree的sum。  
但是，第一个解法是，不管三七二十一，用hash把整个给你统计出来。这个过程是overdone了，实际上是偷懒。
## “只为你需要的付出代价”
这里只需要最高频率的，那么其他频率就不需要浪费空间和时间去整理。   
我先判断最高频率是谁，再去定向整理。
## python细节
max(list)的时候，list不能[]，会报错的
# naive solution
```py
class Solution(object):
    def findFrequentTreeSum(self, root):
        freq = collections.Counter()
        max_freq = 0
        
        def dfs(root):
            if not root: return 0
            ls,rs = dfs(root.left),dfs(root.right)
            s = ls+rs+root.val
            freq[s] += 1
            return s
        
        dfs(root)
        times = collections.defaultdict(list)
        for s,freq in freq.items():
            times[freq].append(s)
        max_times = 0
        res = []
        for t in times.keys():
            if t > max_times:
                res = times[t]
        return res
           
```

# simplified solution
```py
class Solution(object):
    def findFrequentTreeSum(self, root):
        freq = collections.Counter()
        def dfs(root):
            if not root: return 0
            ls,rs = dfs(root.left),dfs(root.right)
            s = ls+rs+root.val
            freq[s] += 1
            return s
        if not root: return []
        dfs(root)
        maxCount = max(freq.values())
        return [s for s in freq.keys() if freq[s] == maxCount]   
```