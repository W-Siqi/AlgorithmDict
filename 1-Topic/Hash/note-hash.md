# 什么时候应该用hash
hash table的广义上的目的都是查找    
但是细分一些情形，更有助于快速嗅到hash的味道
## motivation 1 - 频繁查找
例题：
- 1- two sums
- 149- max points on line(找在同一条直线上的点)
- 336- palindrome pairs(找前缀)
- 710- random pick with blacklist（design题，你要达到快速查找，hash就是一个很好的选择）
- 739- daily temperature(**好题**)（反向遍历构建查找池的一个例子）（这题比hash更加优化的是“过滤筛选”查找法）
- 1044- logest dupliacte substring(和739一样，动态查找池)（难在没意识到，找定长的相同subtring可以做到O(N)）
- 895- maxium frequency stack（**好题**） (design题)（这题交给我的一个道理就是，快速提取hash未必是最优解）（这题最优解释是“分层”的stack的一个巧妙数据结构）
## motivation 2 - 冲突，重复检测，计分板
- 166- fraction-to-recurring-decimal 
- 205- isomorphic (同分异构，检测映射的冲突，hash值的设计有点意思)
- 340- Longest Substring with At Most K Distinct Characters （“at most k distinct”明明白白的冲突检测）
- 1004- grid illumination

## motivation 3 - 快速分组,统计
- 49- group-nangrams
- 711- numbers of distinct islands II (难在提取特征作为hash值，保证特征一致的，放在同一个bucket里) 
- 1224-maxinum-equal-frequency（就是统计谁出现了几次，情形和**895**有点像）
## movivation 4 - 当 bucket
- 41- first miss positive
- 204- count primes

# hash 可能遇见的难点
## 难点1： 没有意识到这可以转化成一个查找问题
比如： 
- 1-two-sum 
- 336- palindrome pairs  
- 1044- longest duplicate substring  

没想到hash，只是自己认出来，这个可以转化为一个查找问题
## 难点2： 没有意识到hash在极端情况是O(N)而不是O（1）
如739- daily temperature. 就是一个hash冲突超级严重的情形。  
又比如一些design的题目，testcase绝对会有一个调皮的输入！
# hash-value的选择
大多数情况下，hash值都是直接用变量本身就行了，python的set和dict自动会帮我们弄。
### float 当key时注意精度
如 76- max points on line
### 其他有意思的hash-value设计
- 1044- longestest duplicate substring （把字符串看做26进制的数字）
- 205- isomorphic
- numbers of distinct islands II（超厉害的hashvalue设计） 