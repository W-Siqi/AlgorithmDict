# TAKEAWAY: sliding window是遍历subarray的排除法
上一次遍历到start，end之后， 本来因为start ++， end重置。  
但是由于一些条件，我们知道 start+1 ~ end 为结尾的，都不用考虑。  
甚至有的时候，我们知道连新的start开始的substring都不是可以的。
## 这里的slding window只是狭义的去寻找子序列，子区间的做法
有时候，two pointers是为了赶其他的事情，不是用来搞slding window 排除法的。
# slding window VS. Dynamic Programming
在subarray，subsequence这种关键词下，slding window 和DP 算是常客。  
下面两题主要就是体现，什么条件，什么情形是slding window还是DP，但是两者皆可
- [978-longest-turbulent-subarray](./978-longest-turbulent-subarray)   
slding window和DP都可以的例子
- [727-minimum-window-subsequence](./727-minimum-window-subsequence.md)   
slding window行不通的情形
# slding windw 常见题型
可能会有更灵活的其他类型，但更重要的是理解他的运作实质，为什么start，end可以这么移动而不漏解（怎么做的排除法）
## a) 找最优subarray
最最最常见  
- [76-minimum-window-substring](./76-minimum-window-substring.md)
- [3-longest-substring-without-repeating-characters](./3-longest-substring-without-repeating-characters)
- [340-longest-substring-with-at-most-k-distinct-characters](./340-longest-substring-with-at-most-k-distinct-characters.md)
- [1004-max-consecutive-ones-III](./1004-max-consecutive-ones-III)
- [1208-get-equal-substrings-within-budget](./1208-get-equal-substrings-within-budget.md)
## b) subarray计数
计数的情形比找最优的复杂，因为最优subarray只求那一个，而计数是要把所有ok的都数上，很难做排除法。
- [992-subarray-with-k-different-integers](./992-subarray-with-k-different-integers.md)  
(这题很有难度，解法也很多)
## c) 定长sliding window  
有个印象很深的就是定长slding window来查duplicated substring:  
[1044-longest-duplicate-substring](./1-Topic/Hash/solutions/1044-longest-duplicate-substring.md)  
还有其他的定长的sliding window的例子，有时候最难的是意识到这是个定长的：
- [567-permutaion-in-string](./567-permutaion-in-string)
- [1052-grumpy-book-store-owner](./1052-grumpy-book-store-owner)
# slding window Implementation
## 常见错误1：漏循环
一定要记住，slding window的实质，是start,end 两层for 进行O(N*N)遍历的简化。  
所以无论两个start，end怎么移动，只要保证这个原则就行了
## 常见错误2：漏解
理论上每次start，end有变动，都需要check一下更新result。  
特别是套两层for，while的，时候更新start或end的时候忘记更新resultle
## 推荐写法
99%的slding window，end 都不需要回溯。  
所以一般最外层用for 循环 end，里面核查start的进位。
