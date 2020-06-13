# traversal: bottom-up/top-down
很多问题，其实就是遍历一下，计算或check某种值。  
这种题，做出来不难，但是写法上要做到思路清晰，而且能one pass遍历的，就不要写多pass记录了。  

## 一次DFS的pass包括了top-down + bottom up
- top-down 是递归调用时，信息从top通过实参一层层往下传
- bottom-up 是递归返回时，信息从bottom通过返回值一层层往上传
  
需要知道 child tree 的信息进而做计算的，就是bottom-up一层层算上去：  
[543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/), [563. Binary Tree Tilt](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/),   
[1123-lowest-common-ancestor-of-](./1123-lowest-common-ancestor-of-.md), [1110-delete-nodes-and-return-forest](./1110-delete-nodes-and-return-forest.md)

有时候，one-pass不够：  
[863-all-nodes-distance-k-in-binaray-tree](./863-all-nodes-distance-k-in-binaray-tree.md)

#  灵魂操作：递归
三段论：左子树，右子树，然后合起来的大树
## recursive defination
- [98-valid-binary-search-tree](./98-valid-binary-search-tree.md)
- [100-same-tree](./100-same-tree.md)
- [508-most-frequent-subtree-sum](./508-most-frequent-subtree-sum.md)
- [110-balanced-binary-tree](./110-balanced-binary-tree.md)
## recursive operation
有时候要对树进行结构性的操作，也可以尝试用递归的去描述她。
- [114-flatten-binary-tree-to-linked-list](./114-flatten-binary-tree-to-linked-list.md)

# 遍历的N种写法
## 递归VS非递归VS Morris
- 非递归：  
速度更快，没有递归调用的开销  
写法上前序遍历很简单，中序和后序稍微复杂  
如果需要top-down,bottom-up传参的话会更复杂，真的要模拟stack的栈帧了
- 递归：  
写法方便，思路直观  
频繁调用，或者嵌套层次大的话，递归本身的开销占了大头  
- Morris：  
https://www.cnblogs.com/anniekim/archive/2013/06/15/morristraversal.html  
核心思路，是利用空的右子树指针存储前驱。  
有点是空间倒是O(1)了，看时间复杂度O(N)是表示怀疑的，因为判断节点的左子树有无遍历，是while loop把剩下的走到底的，这一个过程并不是O(1)

## DFS VS BFS
- 时间复杂度：两者没有太大差别。  
- 空间复杂度：DFS是最大深度，而BFS是最大宽度。所以很多情况下，是BFS的空间要求更高。 当然，这个是要在tree很大的时候，才考虑，而且特殊情况特殊分析。  

带depth的DFS取代BFS
- [102-binary-tree-level-order-traversal](./102-binary-tree-level-order-traversal.md)
- [515-find-largest-value-in-each-tree-row](./515-find-largest-value-in-each-tree-row.md)
- [199-binary-tree-right-side-view](./199-binary-tree-right-side-view.md)

# BST
## list -> BST
递归构建法，选一个数作为中点root，然后递归构建左边和右边
- [95-unique-binary-search-trees-II](./95-unique-binary-search-trees-II.md)
- [96-unique-binary-search-trees](./96-unique-binary-search-trees.md)

## BST -> list
Fact：BST的中序遍历序列，就是排序了的数组
- [[STAR]98-valid-binary-search-tree](./98-valid-binary-search-tree.md)
- [230-kth-smallest-in-BST](./230-kth-smallest-in-BST.md)

- [538-convert-BST-to-greater-tree](./538-convert-BST-to-greater-tree.md
)

# other problems
- [101-symmeric-tree](./101-symmeric-tree.md)
- [572-subtree-of-another-tree](./572-subtree-of-another-tree.md)
- [1104. Path In Zigzag Labelled Binary Tree](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/)(满二叉的编号规律)
- [222-count-complete-tree-nodes](./222-count-complete-tree-nodes.md)(完全二叉树的编号)
- [117-populating-next-right-pointers-in-each-node-II](./117-populating-next-right-pointers-in-each-node-II)
- [112-path-sum](./112-path-sum.md)  ,[437-path-sum-III](./437-path-sum-III.md)
- [1123-lowest-common-ancestor-of-](./1123-lowest-common-ancestor-of-.md)(共同祖先类)
- [1110-delete-nodes-and-return-forest](./1110-delete-nodes-and-return-forest.md)(dfs传递flag避免多个递归)