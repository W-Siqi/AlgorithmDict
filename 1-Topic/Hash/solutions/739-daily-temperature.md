# 从后向前遍历： 构建查找结构
这题的naive是O(N*N),第二个N在于，对于每个数字，都需要往后遍历查找。  
**只要是查找，就很有可能用hash，二分之类的手段优化**  
## 从后向前遍历
由于对于i，我们要查i~n的数字（**这种情形其实很多**），因此，从后向前遍历来扩张查找集合，这样当前的集合总是可是符合要求的备选项。
## 构建查找结构
那么常见的快速查找的结构有哪些手段
- hash
- 排序+二分
- 过滤筛选  

# solution 1（hash）
用hash组织查找数据。  
hash之所以可以的原因，是因为，温度是从30~100.
```py
class Solution(object):
    def dailyTemperatures(self, T):
        res = [0]*len(T)
        seen = collections.defaultdict(list)
        for i in range(len(T)-1,-1,-1):
            # 遍历温度
            for temp in range(T[i]+1,101):
                if temp in seen:
                    if res[i] == 0: res[i] = seen[temp]-i
                    else: res[i] = min(res[i],seen[temp]-i)
            # 维护hash信息，保证存的永远是最前面的day
            seen[T[i]] = i
        return res
```

# solution 2(过滤筛选+stack)
这题的查找标准有2个，一个是温度，一个是index.  
如果一个element，温度又低，idnex有大，那么这个element就被完爆，可以直接丢掉。这样通过减少candidate的数量，来保证遍历对象少。  

### 进一步优化 - stack
如果从后往前遍历，当前的index一定最优的，所以candidate**所有比这个温度小的都可以丢掉**。  
这样很容易想到排序，从大大小排，如果最右边的比这个小，就pop，pop到top的温度比这个大位置，这种情况就可以用stack。      

这一题stack更妙的是，查询的过程和维护stack的是一致的，也就是pop完看一下stack是不是空的就好了（说明有元素index比我大（因为遍历顺序），温度也比我大（不然就被pop掉了））
``` py
class Solution(object):
    def dailyTemperatures(self, T):
        res = [0]*len(T)
        stack = []
        for i in range(len(T)-1,-1,-1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
```

# solution3(hash,我的AC原解)
这题的intuition就是，从前往后遍历，逐步组织hash。  
对于当前day，我可以去反过来更新前面的day的数组（因为查找集是前面的元素，所以是反过来更新）。
##  hash常见的错误：忽略过长冲突退化为list的情况
这题最初的写法是TLE的，因为我的hash，是同一个温度的index全部存下来，而hash的范围是30~100，这样很快就退化为list。  
但是这题很容易优化的地方，就是过滤筛选。一旦一个数被更新了，就可以直接从hash里删掉！因为这已经是最优解了！
```py
class Solution(object):
    def dailyTemperatures(self, T):
        res = [0]*len(T)
        seen = collections.defaultdict(list)
        for i in range(len(T)):
            for temp in range(30,T[i]):
                # some day before is colder
                if temp in seen:
                    # update the day 
                    for index in seen[temp] :
                        res[index] = i-index
                    del seen[temp]
            seen[T[i]].append(i)
        return res
```