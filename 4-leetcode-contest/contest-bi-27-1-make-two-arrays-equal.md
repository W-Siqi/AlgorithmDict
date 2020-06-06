# 这里一个猜想
就是只要你是“同分异构”的排列组合，那么就一定能swap过来。  
## 如何证明？
日后填坑

# “同分异构” 的判定方法
其实之前做过，最简单的就是排序就完事了。  
没必要像我一开始那么傻，真的用hash去统计

# 直白笨办法
```py
class Solution(object):
    def canBeEqual(self, target, arr):
        if len(target) != len(arr):
            return False
        s1,s2 = collections.Counter(),collections.Counter()
        for i in range(len(target)):
            s1[target[i]]+=1
            s2[arr[i]]+=1
        res = True
        for k in s1.keys():
            if k not in s2 or s1[k] != s2[k]:
                res= False
                break
        return res
```

# sort
就1行...  
另外就是[]的判等，这里不是判引用，而是根据list的内容来判等的
```py
 def canBeEqual(self, target, A):
        return sorted(target) == sorted(A)
```