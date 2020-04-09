# 1- Relative Sort Array
## KEY:简单题

# 2- Lowest Common Ancestor of Deepest Leaves
## KEY: 树基础
这题找给定节点，其实就是观察他具有什么属性。  
而对于一个节点来说，能具备的数据不外乎是：  
```
1-自己的val 与前驱传来的关系  
  
2-自己与子节点关系  

3-自己与subtree的关系

4-自己的两个subtree的关系

5-.....
```
这题就是比较两个字数深度的关系， 来确定遍历的方向和终点。
# 3- Longest Well Performing Interval
## KEY:最优区间  
**(类似题目LC525 contagious array)**  

这题的巧解有两个出发点：  
### 1-积分累计法
对于顺序无关的统计量（如这里的），我们可以在遍历的过程中累计score来作为状态标志。   
每个位置的积分，不光可用来判断当前的状态，还可以通过相减判断两个位置之间的状态
### 2-遍历区间
如何找最优区间呢，这里的方法是，从头到尾遍历。  
到i的时候就寻找以i结尾的最优值。    

  
这题就是在遍历区间的过程中有优化，如果当前score是正数，直接从头到尾，如果是负数，直接找比他score小一的最左值。



## 使用？操作符来简化
看看下面的代码:
```
if(hours[i]>8)
    score++;
else
    score--;
```
使用？只有一句的内容
```
score += (hours[i] > 8 ? 1:-1 );
```
# 4-
## KEY: DP 
DP待整理