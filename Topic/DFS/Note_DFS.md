# The dataflow in DFS: top-down and bottom-up
keep the concept in mind. help to code with clear mind.   
## top-down: 
give the chance to pass the history of accumulative value to child.   
## bottom-up: 
give the chance to gather infomation from child and then make judgement based on it

# Strategy Searching
DFS is a very common case to search the strategy.
1. Remove Boxes
https://leetcode.com/problems/remove-boxes/
hard！
2. Shopping Offers
https://leetcode.com/problems/shopping-offers/
3. Strange Printer
https://leetcode.com/problems/strange-printer/
类型同上？

# The recursive defination
The data structure 'tree' itself is defined recursively.   
So the formula to check a tree is:  
a. check left child  
b. check right child  
c. check root
1. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

2. Same Tree
https://leetcode.com/problems/same-tree/

3. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
判断一个树是不是balance的，也就所有子树，childen左右的高度差不超过1

4. Symmetric Tree  
https://leetcode.com/problems/symmetric-tree/
判断一个树是不是中心对称的

# Answer Searching
the simplest scenario:   
if we want to find the optimal answer, just  traverse it and update min/max value of something equal.
1. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/


2. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/


# Path of the tree
path the history in the **top-down** dataflow. When reach the leave node. There is the path.  

In most cases, we can use **Backtraing** to skip the tedious memory assign, which is performance friendly. 
1. Path Sum
  https://leetcode.com/problems/path-sum/  
If there is a path that the sum of data is equal to the given value.
2. Path Sum II
https://leetcode.com/problems/path-sum-ii/
Find and print all paths that the sum of data is equal to the given value.
3. Insufficient Nodes in Root to Leaf Paths
https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/  
delete all node: that all path through this node is the path with sum less than a given value.    
(PS: This can use bottom-up method to make an decision accroding to children's situations)
4. Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/  
every node stands for 1-9. So each path stands for a number. Sum all numbers form in this method.  
(PS: this can be both top-down and bottom-up. In the bottom-up, sum += depth * value * numberOfChildren)


# BFS VS DFS
When it comes to 'each row' related probelm. It is very easy to use BFS.   
But with DFS with more attention about depth, we can solve it with less and more clean code.
1. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/  
just alway try to traverse the right child.
2. Find Bottom Left Tree Value
https://leetcode.com/problems/find-bottom-left-tree-value/
BFS简单，想一想怎么用DFS！
3. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/  
(PS: just maintain a global list recoding the current largest value)

# Other
1. Lowest Common Ancestor of Deepest Leaves
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
寻找两个深度最高的叶节点的，深度最大的公共祖先

1. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
把一个二叉树展平成一个链表

3. Delete Nodes And Return Forest
https://leetcode.com/problems/delete-nodes-and-return-forest/
删掉一系列的节点后，返回剩下的所有的树（即森林）