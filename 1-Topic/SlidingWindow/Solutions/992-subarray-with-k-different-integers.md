# 计数问题：超恶心的slding window排除法
sliding window 移动start，end的依据是排除法，这个在找最优subarray或者是否存在，是很容易的。  
但是这题是需要计数，有多个符合要求的都要算进去，所以上排除法很恶心    

**而且有个地方要end回溯！**，就是start 前进后，是新的number，那么就要老老实实重start+1重头算，而且这种情况十分常见啊！
```py
for end 一直移动一边计数：
    if(end 发现要超过K了)：
        start += 1
        if(start加1后变回K次了)
            end 继续推进
        elif(start加1后还是K+1次)
            快速计数：
                if 刚删掉的数和此前一样：
                    就是start-1的结果减去1
                else:
                    # end 要回溯！
                    完全重算 
            继续推start
```
# Solution 1 - 问题转化
exactly K 很难数，但是at most K 就很好数了，因为at most K 就是个找最优subarray的问题（最长的符合atmostK的sub array）  
然后 exactly（K） = atmost（K） - atmost（K-1）

# Others Solutions
这题如果不按套路解,确实有点难...  
其他解法：  
 
https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235235/C%2B%2BJava-with-picture-prefixed-sliding-window  

https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/360147/Share-my-solution