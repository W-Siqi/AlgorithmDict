# 策略搜索
## 策略搜索与DP
策略的搜索，很多时候都要用到memorization，也就是DP。  
其动机有：  
1. 策略搜索都是指数的复杂度，短短一二十个step就会让你超时
2. 策略搜索都会基于当前的“上下文”做出下一步，而“上下文”很多时候就是一个重叠的子问题
  
Remove Boxes
https://leetcode.com/problems/remove-boxes/    
Brust Balloons 
https://leetcode.com/problems/burst-balloons/

Shopping Offers
https://leetcode.com/problems/shopping-offers/  

Strange Printer
https://leetcode.com/problems/strange-printer/

## 老老实实的暴力搜索


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