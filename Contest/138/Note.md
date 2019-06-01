# GrumpyBookstoreOwner

# 4 - Distant Barcodes
## Test Case Filures
    [7,7,7,7,5,5,5,5,8,8]  
不能+2，+2这么插，这样太极限了  

    [51,83,51,40,51,..] 很长，反正就是最后一列不止一个爆出范围
之前看到一个溢出的testcase，就以为只会溢出一个..naive
而且，break要改成continue，被过去思维所限制

# Other Tips
注意一下 NOTE， 如果size，length 有上万的话，可能会卡runtime的，这种用嵌套循环搞不好就直接挂了。如果是100、200之类，才可以所欲为。

# Bug Log
## 对溢出的警觉感

## 找最大/最小的标准写法
初始化不要有问题

## 边界值忘记考虑
Distance Board, 不是每次都要+2？

## 忘记break
还是那个老毛病，特例执行的时候，忘记continue，把下面的也执行了一遍

## 改错改一半
带break 和 counter的for循环， 在修改的时候十分容易出错