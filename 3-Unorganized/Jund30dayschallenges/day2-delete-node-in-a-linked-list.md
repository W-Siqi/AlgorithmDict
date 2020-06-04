# 注意，这里删节点，是不给前驱prenode的！
## 核心思路
删节点和改变值，解耦  
删的节点的值不一定是那个节点，我们只要保证最后的值移对了就行

# solution 1  - O(N)  
有点像数组删值，逐个往前推
```py
class Solution:
    def deleteNode(self, node):
        p = node
        while True:
            p.val = p.next.val
            if not p.next.next:
                p.next = None
                break
            p = p.next
```
# solution 2 - O(1)
但注意，这是链表！没必要像solution 1 那么蠢。  
其实后面大部分的节点都是不用动的，可复用的。  
所以我们不如只删后面一个: **即把当前的val,next完全拷贝next，然后把next删掉**
```py
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```