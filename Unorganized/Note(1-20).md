# 5 - ContainerWithMostWater

## 5.1 - C++max/min
包含在c++标准库中头文件<algorithm>中，在头文件<windows.h>中定义了min,max的宏，
若在包含<algorithm>的同时包含<windows.h>会导致函数无法使用   

example:  

    a=max(a,val);  
    b=min(b.val);

## 5.2 - 剪枝
我R10的那个版本是暴力遍历，但是对于这种求max，min的，如果在一次遍历中可以估算预期最大值，就可以剪枝。  
比如当前高为h，就算它宽拉满也比不过现在的max，那么这一波就直接continue了  
于是就是有了R20版本，速度快了3倍 ！

## 5.3 最优解
这里还有O（n）的方法，但是我还法子证明他为什么work，先留着