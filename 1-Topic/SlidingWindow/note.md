# TAKEAWAY: sliding window是遍历subarray的排除法
上一次遍历到start，end之后， 本来因为start ++， end重置。  
但是由于一些条件，我们知道 start+1 ~ end 为结尾的，都不用考虑。  
甚至有的时候，我们知道连新的start开始的substring都不是可以的。

# slding window 实践手册
## 常见错误1：漏循环
一定要记住，slding window的实质，是start,end 两层for 进行O(N*N)遍历的简化。  
所以无论两个start，end怎么移动，只要保证这个原则就行了
## 常见错误2：漏解
理论上每次start，end有变动，都需要check一下更新result。  
特别是套两层for，while的，时候更新start或end的时候忘记更新resultle
## 推荐写法
99%的slding window，end 都不需要回溯。  
所以一般最外层用for 循环 end，里面核查start的进位。

# slding windw 常见题型
## 找最优subarray
[76-minimum-window-substring](./76-minimum-window-substring.md)
## 检查某种subarray是否存在
## subarr计数