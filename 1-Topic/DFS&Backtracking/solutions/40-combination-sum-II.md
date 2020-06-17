# 排列组合（同leetcode-39）
## sort vs hash
这题避免重复，简单的做法就是把数字相同的聚在一起。  
一开始我是直接排序了。  
但是用个hash Counter更快，因为是O(n),而且我不在乎顺序。
## 一个TLE提交
我忘记剪枝了，target超限因为是positive number，所以减掉。  
DFS里面这种剪枝速度的提升，在有的test case下可能是几何倍数的...所以千万别忘了
# solution
```py
class Solution(object):
    def combinationSum2(self, candidates, target):
        items = collections.Counter(candidates).items()
        res = []
        def dfs(index,target,path):
            if target == 0:
                res.append(path)
                return
            if index >= len(items):
                return        
            num,count = items[index]
            for i in range(count+1):
                if target - i*num < 0:
                    break
                dfs(index+1,target-i*num,path+[num]*i)
            
        if candidates:
            dfs(0,target,[])
        return res
```