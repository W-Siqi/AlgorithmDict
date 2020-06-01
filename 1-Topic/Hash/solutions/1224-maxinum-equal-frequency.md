# 启示：简洁写法的力量
我这题虽然AC了，但是写出来的解有三四十行。  
而大佬的解只有一二十行，**这是需要警惕的地方！**  
我们的思路几乎没差，但是人家比我简洁，虽然都AC，但是有本质差别！  
简洁意味着：  
- 整个逻辑思路很简洁，出bug几率小，查bug也方便
- 面试写代码的时候，更流程，面试官更容易看明白，自己也写得更快

todo:  
以后每次contest，一定要看一下优秀的代码。  
把代码的简洁性纳入标准，包括语言简洁和逻辑简洁。
## 不要过分追求极致简洁
高度同一化的写法是很精妙的写法。像6行二分法那种高级精妙，同一化的简洁，是需要背后成吨的思考的。  
而面试的目的，是直白直觉的写出来。  
所以这里简洁的追求主要
1. 简化冗余的分支，和unessary的check
2. 运用语言特性不要写蠢方法
3. 一些如musk之类的trik
4. 设置默认值这些简单的同一化写法...
5. ....

# python collecton.counter()
hash map做计数板很恶心的一个地方，要先判断key在不在，来选择是初始化为0，还是+=1.  
如果key不在，+=1会出现key error报错  
    
这里我们的collection.counter()就派上用处了：  
counter是python里面dict的一个子类：
更多子类了解：  
https://blog.csdn.net/Shiroh_ms08/article/details/52653385

# if/else的艺术
if 和 else平时写了无数次了，但是都是些简单的情况。  
LeetCode会出现比较复杂的情形，所以要思考一下if/else流程控制的艺术， 包括:  
会不会漏一些情形？  
如何简化多层的if else  
如何避免不必要的 if/else(采用默认值,同一化的写法)
# naive solution - 超繁琐
```py
class Solution(object):
    def maxEqualFreq(self, nums):
        def canRemoveOne(occur):
            if len(occur) > 2:
                return False
            
            if len(occur) == 1:
                k = occur.keys()[0]
                if k == 1 or occur[k] == 1: return True
                else: return False
            
            if len(occur) == 2:
                k1,k2 = min(occur.keys()[0],occur.keys()[1]),max(occur.keys()[0],occur.keys()[1])
                v1,v2 = occur[k1],occur[k2]
                if v1 > 1 and v2 > 1:  return False
                if v1 == 1 and k1 == 1: return True 
                if v2 == 1 and k2 - 1 == k1:  return True
        
            return False
        
        record = {}
        occur = {}
        res = 0
        for i,n in enumerate(nums):
            if n in record:
                record[n] += 1
                # add record[n]
                if record[n] in occur: occur[record[n]] += 1
                else: occur[record[n]] = 1
                # remove record[n]-1
                occur[record[n]-1] -= 1
                if occur[record[n]-1] == 0:  del occur[record[n]-1]
            else:
                record[n] = 1
                # add record[1]
                if 1 not in occur:  occur[1] = 1
                else:  occur[1] += 1
            # print(canRemoveOne(occur),occur)
            if canRemoveOne(occur):
                res = max(res,i+1)
        
        return res
```

# 简洁1.0 版本
一个是用了collection.counter  
还有就是简化了if的流程：
1. 去除不必要的if  
canRemoveOne()里面，if(len(occur) > 2)这个是废话，因为我的真的判定模式是，**if来抓true，然后默认返回false(很常见的情况判断逻辑)** 然而，这个if用来抓false不是很必要
2. “嵌套改成串行”  
前面的嵌套特别深，因为顶层用了if来区分原来的key在或不再。但其实后面更新freq的时候，**自己独立知道如果更新**，所里没必要放在这个if下面，这是一个偷懒的行为！
```py
class Solution(object):
    def maxEqualFreq(self, nums):
        def canRemoveOne(occur):
            # 修改的地方1:多余的if
            # if len(occur) > 2:
            #     return False
            
            if len(occur) == 1:
                k = occur.keys()[0]
                if k == 1 or occur[k] == 1: return True
                # 修改的地方1:多余的if
                # else: return False
            
            if len(occur) == 2:
                k1,k2 = min(occur.keys()[0],occur.keys()[1]),max(occur.keys()[0],occur.keys()[1])
                v1,v2 = occur[k1],occur[k2]
                # 修改的地方1:多余的if
                # if v1 > 1 and v2 > 1:  return False
                if v1 == 1 and k1 == 1: return True 
                if v2 == 1 and k2 - 1 == k1:  return True
        
            return False
        
        # 修改的地方2
        record,freq = collections.Counter(),collections.Counter()
        res = 0
        for i,n in enumerate(nums):
            record[n] += 1
            freq[record[n]]+=1
            if record[n] > 1: 
                freq[record[n]-1] -= 1
                if freq[record[n]-1] == 0:
                    del freq[record[n]-1]
            if canRemoveOne(freq):
                res = max(res,i+1)     
        return res
```

# 简洁2.0版本(追求极致)
描述情况的角度：  
我原来有4种情况是可行的： 
1. 所有number都只出现1次
2. 只有一种number出现了n次
3. 有出现了n次和n-1的，而且出现n次只有一种number
4. 有出现了n次和出现了1次的，而且出现1次的只有一种number   
 
## 目前认为，不要为了过分追求极致简洁，而牺牲直白性和直觉性。
### 版本1，用maxfreq来描述
我原来的是“暴力描述”，即需要知道所有信息，然后直白地去描述，因此，我要小心维护freq,比如次数为0的要del掉。  
但其实只需要知道，“出现”次数的最大值n就行了，其他的都可以推出来。 
```py
# 虽然这个很简洁，但是不直白，容易被绕晕
class Solution(object):
    def maxEqualFreq(self, nums):
        record,freq = collections.Counter(),collections.Counter()
        res,maxFreq = 0,0
        for i,n in enumerate(nums):
            record[n] += 1
            freq[record[n]]+=1
            if record[n] > 1: freq[record[n]-1] -= 1
            
            maxFreq = max(maxFreq,record[n])
            remain = i + 1 - maxFreq * freq[maxFreq]
            # 4种情况
            if maxFreq == 1:  res = i + 1  
            elif maxFreq * freq[maxFreq] == i+1 and freq[maxFreq] == 1: res = i + 1
            elif remain == 1: res = i + 1
            elif maxFreq + (maxFreq-1)*freq[maxFreq-1] == i + 1: res = i + 1
        return res
```
### 版本2
说的是two cases， 但从他的理解来看，第二个case，还是包括了很多子case。

https://leetcode.com/problems/maximum-equal-frequency/discuss/403743/JavaC%2B%2BPython-Only-2-Cases%3A-Delete-it-or-not
```py
 def maxEqualFreq(self, A):
        count = collections.Counter()
        freq = [0 for _ in xrange(len(A) + 1)]
        res = 0
        for n, a in enumerate(A, 1):
            freq[count[a]] -= 1
            freq[count[a] + 1] += 1
            c = count[a] = count[a] + 1
            if freq[c] * c == n and n < len(A):
                res = n + 1
            d = n - freq[c] * c
            if d in [c + 1, 1] and freq[d] == 1:
                res = n
        return res
```
## 回过来看我改善后的直白版本,流程还是比较清晰的，也没臃肿多少
```py
class Solution(object):
    def maxEqualFreq(self, nums):
        def canRemoveOne(occur):         
            if len(occur) == 1:
                k = occur.keys()[0]
                if k == 1 or occur[k] == 1: return True
            
            if len(occur) == 2:
                k1,k2 = min(occur.keys()[0],occur.keys()[1]),max(occur.keys()[0],occur.keys()[1])
                v1,v2 = occur[k1],occur[k2]
                if v1 == 1 and k1 == 1: return True 
                if v2 == 1 and k2 - 1 == k1:  return True
        
            return False
        
        record,freq,res = collections.Counter(),collections.Counter(),0
        for i,n in enumerate(nums):
            record[n] += 1
            freq[record[n]]+=1
            if record[n] > 1: 
                freq[record[n]-1] -= 1
                if freq[record[n]-1] == 0:
                    del freq[record[n]-1]
            if canRemoveOne(freq):
                res = max(res,i+1)     
        return res
```