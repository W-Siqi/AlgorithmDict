# 策略搜索
## a)策略的DP动机
策略的搜索，很多时候都要用到memorization，也就是DP。  
其动机有：  
1. 策略搜索都是指数的复杂度，短短一二十个step就会让你超时
2. 策略搜索都会基于当前的“上下文”做出下一步，而“上下文”很多时候就是一个重叠的子问题

## b)如何判断策略搜素的时候是否DP？
**99%的策略决策都会重复出现子问题，但并不代表可以DP**

很大的一个分界线就是，下一步之后的策略，是否是“self-contained”的, 也就是是否以来前面的决策的上下文。   
经典例子就是数独和八皇后问题，做决策需要之前面的信息；   而字符串匹配，分割，不需要之前面是怎么分的， 我只要知道前面是分割成功这个结果就行了。  

### 子问题是self-contain的：
10和140都是字符串匹配问题，不要以为，按照step的，策略决策就不会出现重叠的子问题  
- [10-regular-expression-matching](./10-regular-expression-matching.md)  
- [140-word-break-II](./140-word-break-II.md)  

### 子问题不是self-contain的，要基于前面的决策：
- [37-sudoku-solver](./37-sudoku-solver.md)      
- [51-N-Queens](./51-N-Queens.md)   
无阶段的策略种决策种避免重复  

## c)其他例子
Remove Boxes
https://leetcode.com/problems/remove-boxes/    
Brust Balloons 
https://leetcode.com/problems/burst-balloons/

Shopping Offers
https://leetcode.com/problems/shopping-offers/  

Strange Printer
https://leetcode.com/problems/strange-printer/

# grid网格寻径
## BFS VS DFS
grid里面的遍历实质上，就是对图的遍历，比树的遍历要多一个避免回路的步骤  
- DFS: 记录走过的路径，要么传递path，优化传递的话可以用backtracking
- BFS: 记录已扩张过的点  

但其实下面的几个题目，都是BFS比DFS更好,主要原因是：  
1. BFS 更直观，更容易想象
2. BFS 可以知道全局信息，比如要计算全grid的可抵达性或路径，都是BFS更直接方便.   
## 常见寻径情形
### a)点到点 
- [1391-check-valid-path](./1391-check-valid-path.md)
### b)点到区域 
- [417-pacific-atlantic-water-flow](./417-pacific-atlantic-water-flow.md)
- [542-01matrix](./542-01matrix.md)
### c)区域到区域
- [934-shortest-bridge](./934-shortest-bridge.md)
## 带权值/能耗函数 怎么办？


# 排列组合
## 枚举 or 是计数/求最优  
如果是枚举，那么就是老老实实的搜索。   
如果是计数/求最优， DP八成是要安排上的。
## 排列or组合
- 组合，也就是求subset这种，决策过程往往是其i个选or不选进行分支  
- 排列，决策过程就是，第i个元素选哪个
## 组合问题
组合问题的第一大问就是，处理好duplication问题！   
比如求subset，通常要对元素排序，避免重复数了同一个subset
- [90-subset-II](./90-subset-II.md)  
求组合的“hello world”
- [39-combination-sum-I](./39-combination-sum-I.md)
- [40-combination-sum-II](./40-combination-sum-II.md)  
 通过聚合避免重复，同时是一个搜索中剪枝大大提升速度的例子
 - [77-combinations](./77-combinations.md)  
 这题可以当排列问题做，也可以当组合问题

## 排列问题
- [1079-letter-tile-possibilities](./1079-letter-tile-possibilities.md)
- [17-letter-combinations-of-a-phone](./17-letter-combinations-of-a-phone.md)
