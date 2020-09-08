# 2. add two numbers
- 5+5 = 10这种edgecase 别忘了，很容易看两个pointer都走到头了就while loop break了

# 4. Median of Two Sorted Arrays
- 这里就是注意简化if/else， 因为每轮必会挑选1个队列，所里第一个if把符合的情况全部列出来，剩下的else到另一个就ok 了
- 这里出现一个笔误，index1比index2小，其实你要提醒自己的话，就应用indexFormer,indexLater之类的...

# 11. Container With Most Water
-  一个比较经典的贪心法，其实这题的贪心，基于排除。为了寻求更大解，只能这么走！
- 注意while的逻辑，“移动到符合条件的index” == 只要不符合条件，就++

# 19. Remove Nth Node From End of List
- 其他的解法很简单，但是要做到one pass 就没那么容易啦

# 22. Generate Parentheses
- n对括号怎么摆，是个排列问题，按照n个step进行搜索就行了

# 23. Merge k Sorted Lists
- 教训，忽略数据结构操作的本身开销

# 45. Jump Game II
- 直接用DP会超时，因为检查的状态太多了
- 方案1： 改成贪心，O(N)解决
- 方案2： 维护DP遍历的set，进行淘汰筛选。

# 55. Jump Game
- 和45. Jump Game 一样，因为每次更新的时候遍历导致超时
- 解决方案也类似，就是缓存最优解，从而避免遍历

# 56. Merge Intervals
- 排序+遍历就完事儿，easy 

# 70. Climbing Stairs
- easy DP， 重叠子问题不要太明显
- 但也别忘了最初的暴力法是怎么来的

# 53. Maximum Subarray
- 就是有个很骚包的divide&conquer解法...

# 42. Trapping Rain Water
- 遍历找max/min：“DP”  
这题的暴力，是对于每个i，找左边最高和右边起最高。但是其频繁找max，有很多“重叠子问题”。我们不如用O（n）先把leftmax和rightmax给弄了。
- 解法2：双指针，移动height小的那个，因为这样保证的对面的height肯定不这边目前的max要大，所以只要这边的max就ok了。
- 错误解法： 找坑，就是找先下降，后上升的那个坑，然后坑里的池就好计算了。 但可能那个坑是个“海底坑”，整个坑都在更大的一个池子里....

# 33. Search in Rotated Sorted Array
- 这题印象太深了： 第一个数nums[0]是横截点，比这nums[0]大的都是左边的，否则都是右边的；这样就是用二分法切分成2个数组。

# 136. Single Number
- 一个XOR(^)的小技巧， a^a == 0, a^0=a 
- C++里，别忘了^,|,&这三个位运算符哈

# 128. Longest Consecutive Sequence
- hash的名场面，体会一下

# 79. Word Search
- 2d Grid 做backtracking的一点就是，记录seen直接在grid上标记，遍历完了记得抹去就ok，而不是每次去传个set，这样就麻烦了。

# 48. Rotate Image
- 这种题目一定要勤画图！ 脑补真的一恶心地一匹让人不想动，但是笔这么一画就超清楚了！
- 坐标旋转，一些坐标变换的数学定律记一下

# 75. Sort Colors
- 结论：无论是快排的分2组，还是这题的分三组，都有one- pass解法
- 原理就是两边排指针维护“栈顶”，中间遍历往两边推
- 为什么这样work，这样work的就是个奇迹，感觉像是直觉出算法，然后去证明。因为换过到栈顶的元素，是很安心的保证正确的，但是换过来的行为就有点不可预知了...

# 138. Copy List with Random Pointer
- 这题很有通用实用价值，就是你怎么深层拷贝一个类（带乱七八糟指针指来指去的时候）

# 124. Binary Tree Maximum Path Sum
- 就是一个bottom up的东西，不配hard

# 152. Maximum Product Subarray
- 经典的DP情形，subArray的和
- 这题其实你在暴力遍历的时候，就能感受到重叠的子问题

# 169. Majority Element
- hash可以做到O(N), 但这题有一个更巧妙的解法。  
  
# 739. Daily Temperatures
- hash专题做过，但是最优解是用stack，这个和 239. Sliding Window Maximum 的思想很像，淘汰机制。如果顺序和大小都完爆，那就筛掉
    
# 283. Move Zeroes
- 比较经典的，直接element往前移，one pass. （其实这是有应用情形的，就是一次性排干数组里的无效element）

# 215. Kth Largest Element in an Array
- 找第K大的经典算法，快排，堆排，排行榜，quickselect快速选择，一个都不能少哈


# linked-list的教科书练习题
## 160. Intersection of Two Linked Lists
两种思路，1）hash查询，2) two pointers使得相遇在交叉点
## 142. Linked List Cycle II
那个龟兔赛跑的算法..

## 148. Sort List
基于链表排序最难的是，不能随机访问  
BUT: merge sort是不需要随机访问的！  
- Q: 链表怎么快速取中点?  
- A： 一个quick，一个slow，quick到底的时候，slow就是在中点了

## 206. Reverse Linked List
链表hello world级别的，不多说

## 234. Palindrome Linked List
1. 转array，用two pointer
2. 一个quick + slow 找出中点，然后把后半截翻转，再按照two pointers
3. 【妙】递归


# Tree的教科书练习题
## 非递归遍历系列
### 94. Binary Tree Inorder Traversal
最简单，访问自己，push
### 144. Binary Tree Preorder Traversal
cur+stack 模式： cur**要么从parent滑过来，要么从stack取**   
一个节点会过2次cur指针：
- 第一次： cur 转到左边
- 第二次： 访问自己，cur 转到右边
### 144. Binary Tree Postorder Traversal
（这个最麻烦是因为： 我们需要额外的一个stack来追踪这个节点是第几次光顾了，preorder是因为第二次是从stack.pop出来，第一次是因为指针递归）   
还是cur+stack模式： 但是1个节点会过3次cur指针：
- 第一次： cur 转到左边
- 第二次： cur 转到右边
- 第三次： 访问自己，cur放置空(或者立马从stack取)
## 二叉树构建
### 105. Construct Binary Tree from Preorder and Inorder Traversal
构建需要满足的要求：  
1. 必须有中序，然后加一个后序/前序。因为要找root进行递归
2. 不能重复元素，否则就不是唯一解。（比如[1,1,1,1,1]和[1,1,1,1,1]两个就有多种构建方法）
# Design
## 146. LRU Cache
有实际场景的一道题。  
hash存指针，用来快速定位链表。  
事实上，hash用来辅助查询，就是用这种存指针，而真正数据在指针后的数据结构里

## 155. Min Stack
- 这里非O（1）的阻碍，是min的那个值被pop了之后，需要重新遍历找min
- 然鹅这种重新遍历是可以避免的... 因为你push的过程，其实就是把min遍历一遍了，所以只要缓存结果进stack就行了
## 380. Insert Delete GetRandom O(1) 
- hash辅助查找的复合结构,hash存vector的index
- vector的删除和增加是可以做到O(1)的！（如果不用保证顺序的话）

## 295. Find Median from Data Stream
- 经典的双heap解法，其实持续插入＋维护排序，基本也就heap了

# 感受贪心
## 406. Queue Reconstruction by Height 看出贪心
这题核心问题，就是在队列里面，互相有约束。   
**约束问题，是贪心法比较常用的情形**:
1. 每一步必须满足当前约束 （前面必须有k个不比他矮的）
2. 每一步尽量放宽后面的约束 (尽量往后移动，使得高的尽量靠后，这样后面插入的大致都是递增。而且尽量不打乱后面的约束条件)   
至于这题怎么证明想通贪心，一个观察就是“矮的随便怎么放，都不影响比它高的结果. 但是高若在矮的前面，会影响比它矮的结果” -> 高的尽量靠后

## 621. Task Scheduler（已单独记录）
很明显的贪心，为了充分利用，当前可数最高的优先

# to-do
- 84. Largest Rectangle in Histogram
- 32. Longest Valid Parentheses
- 72. Edit Distance
- 207. Course Schedule（拓扑排序）
- 301. Remove Invalid Parentheses(一堆括号的)
- 416. Partition Equal Subset Sum（这个DP？？）
- 221. Maximal Square (这个DP怎么破？)
- 253. Meeting Rooms II 非暴力解我好像没想出来...
- 279. Perfect Squares 策略搜索引发的DP，但是soltuion似乎有一大堆更高端的解？
- 338. Counting Bits  这题的DP真的骚...



array的DP
- 581. Shortest Unsorted Continuous Subarray 累加max/min的那个技巧
- 238. Product of Array Except Self
- 152. (已记录)
- 647. Palindromic Substrings 好像有O（N）的解法？？？
- 300. Longest Increasing Subsequence 最经典的DP，了解他的一切！暴力怎么弄，DP怎么弄，O(nlgn)怎么弄？



