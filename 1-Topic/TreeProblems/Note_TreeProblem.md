# BST
## list & tree 转换
### list -> BST
递归构建法，选一个数作为中点root，然后递归构建左边和右边
- [95-unique-binary-search-trees-II](./95-unique-binary-search-trees-II.md)
- [96-unique-binary-search-trees](./96-unique-binary-search-trees.md)

### BST -> list
Fact：BST的中序遍历序列，就是排序了的数组
- [[STAR]98-valid-binary-search-tree](./98-valid-binary-search-tree.md)
- [230-kth-smallest-in-BST](./230-kth-smallest-in-BST.md)

- [538-convert-BST-to-greater-tree](./538-convert-BST-to-greater-tree.md
)
# traversal: bottom-up/top-down
很多问题，其实就是遍历一下，计算或check某种值。  
这种题，做出来不难，但是写法上要做到思路清晰，而且能one pass遍历的，就不要写多pass记录了。  

## 一次DFS的pass包括了top-down + bottom up
- top-down 是递归调用时，信息从top通过实参一层层往下传
- bottom-up 是递归返回时，信息从bottom通过返回值一层层往上传
  
需要知道subtree 的信息进而做计算的，就是bottom-up一层层算上去：  
[543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/), [563. Binary Tree Tilt](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

有时候，one-pass不够：  
[863-all-nodes-distance-k-in-binaray-tree](./863-all-nodes-distance-k-in-binaray-tree.md)

#  recursive defination
三段论：左子树，右子树，然后合起来的大树
- [98-valid-binary-search-tree](./98-valid-binary-search-tree.md)
- [100-same-tree](./100-same-tree.md)
- [508-most-frequent-subtree-sum](./508-most-frequent-subtree-sum)
- [110-balanced-binary-tree](./110-balanced-binary-tree.md)

# 不同写法之间的抉择
## 递归VS非递归
## DFS VS BFS
带depth的DFS取代BFS
- [102-binary-tree-level-order-traversal](./102-binary-tree-level-order-traversal.md)
- [515-find-largest-value-in-each-tree-row](./515-find-largest-value-in-each-tree-row.md)
- [199-binary-tree-right-side-view](./199-binary-tree-right-side-view.md)
# other problems
- [101-symmeric-tree](./101-symmeric-tree.md)
- [572-subtree-of-another-tree](./572-subtree-of-another-tree.md)
- [1104. Path In Zigzag Labelled Binary Tree](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/)