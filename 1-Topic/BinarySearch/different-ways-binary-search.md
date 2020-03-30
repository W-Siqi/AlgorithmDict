# 你可知，这二分，有几种写法？
下面，按照应用情形：
### 1-单纯查找是否存在
最正宗的binary search
### 2-找下界 lower bound(可以等于target)  
[1,2,3,4,5,7(lower bound index),7,7,7,7,8,9]
### 3-找上界 upper bound(一定大于target)  
[1,2,3,4,5,7,7,7,7,7,8(upper bound),9]
### 4-bool形式下的查找
像求一个int的平方根，这种就会通过尝试目标是否 work
## 实际需要几种写法？
可以规约为upper bound 和 lower bound 两种  
是否存在，直接用lowerbound或upperbound 都可以  
bool形式，就当做00000001111111111里去找0或1的上界或下界

# 二分的银弹写法
upper bound 写法这类问题，和有些leetcode一样，想法很简单，但是魔鬼在细节，超多的edge case，现场写很容易搞混了。
## 核心思路：while loop做的是divide两边,而不是塌缩中间
左开右闭[lo,hi) + 这个写法的关注点不是[lo,hi)，而是两边的：  
1. [first,lo) **严格小于**target的
2. [hi,last) **大于等于**target  
缩小lo和hi的目的，是吧list划分为两个区间。  
即当lo==hi的时候。 [first,lo)和[hi,last) 正好把list分成两半，而后面一半的第一个，自然就是下界lower bound
### 所以，最后lo==hi的时候，lo指向的永远是右边区间的第一个元素 

## 标准写法
```py
# edge case: 
def lower_bound(li,target):
    lo,hi = 0,len(li) # 左闭右开
    while lo < hi:
        # mid取 first + (last-first)//2  ,一定要保证：lo = mid + 1 防止死循环
        mid = first + (last-first)//2
        if li[mid] < target: # 求upper bound 的话，< 变成 <= （if li[mid] <= target：)
            lo = mid + 1 # 包括mid，纳入左边
        else:
            hi = mid # 包括mid，纳入右边 
    return lo # reutrn hi 也可， 反正他们的值是一样的
```  

# edge cases分析 
## a) 当target有duplication
[1,2,3,4,8,8,8,8,9,12],  target = 8

[lower,upper)这区间就是所有target。其实lower bound和upper bound这个名字由来，就是这里..

## b)当target只有一个
[1,2,3,4,8,9,12],  target = 8  
lower bound == 4  
upper bound == 5  
合理， 因为8在[4,5)区间嘛

## c) 当target 不存在
这是最最最恶心的
### case1 - [1,2,3,4,9,12], target = 8 
如果是lower bound，落在9  
如果是upper bound，**依然落在9**  
这很好理解，lo,hi 划分为[1,2,3,4] 和 [9,12] **lo==hi 永远落在右边区间的第一个元素**  

### case2 - [22,33,44,456,768] , target = 8 
lo == hi == 0 落在index = 0， 此时整个数组都是右边区间  

### case3 - [1,2,3,4,5,6] , target = 8 
lo == hi == 6， 此时整个数组都是左边区间, lo 越界 

## d) - [] 空数组
以lo == last = 0 返回  
返回值 == len(list)
# 总结
lowerbound 和 upperbound其实就是银弹写法，适配所有的edgecase
1. 当target存在的时候[lowerBound,upperBound)，任何情况下都是target所在的区间。
2. 当target不存在的时候，找lowerBound和upperbound 得到的是同样的结果。返回值永远是右边区间的第一个元素（因此，可能为index == last 越界，此时表示所有元素都比target小）。 