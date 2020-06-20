# 排列组合-subset：处理duplication
这里的duplication在于，父集合有重复的数。  
避免duplication做法和40-combination-sum-II一致，聚合相同的元素，放在同一个step里面。
## 为何不会像40-combination-sum-II要考虑重复前缀的问题？
因为这个的写法，是只会在搜索的叶节点返回，不存在中间返回。也就是path都是从root到leaf是定长的。  
而combination-sum-II会中断返回，所以1,2,3会返回，1,2,3，null会返回， 1，2,3，null,null... 同一个前缀会被不同长度的path返回一遍，
```py
class Solution(object):
    def subsetsWithDup(self, nums):
        items = collections.Counter(nums).items()
        res = []
        def dfs(index,subset):
            if index >= len(items):
                res.append(subset)
                return
            num,count = items[index]
            for i in range(count+1):
                dfs(index+1,subset+[num]*i)
        dfs(0,[])
        return res
```