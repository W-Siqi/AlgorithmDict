# 深层拷贝一个类
## 看做一个graph
因为类的指针和引用是可能互相来，循环引用的。  
所以这个的通用情形，**是如何拷贝一个graph（包括点和边）**   
## 避免重复拷贝。
拷贝graph的节点和边，按照BFS或DFS这么来，会出现重复拷贝。  
所以需要一个map来记录，哪些节点已经拷贝过了

# solution 1 - 先拷贝完所有的节点，再遍历链接引用
```c++
class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> newNodes;
        newNodes[nullptr] == nullptr;
        Node* p = head;
        while(p){
            newNodes[p] = new Node(p->val);
            p = p->next;
        }
        p = head;
        while(p){
            newNodes[p]->next = newNodes[p->next];
            newNodes[p]->random = newNodes[p->random];
            p = p->next;
        }
        return newNodes[head];
    }
};
```

# solution 2 边拷贝边链接引用
这个和solution 1本质上是一样的。  
写起来复杂点，但是one pass

# solution 3 这题的特殊解 - 用顺序作映射关系
two-pass 但是不需要额外空间。    
就是第一遍拷贝不是拷贝单独的list，而是node-x的复制就挂在node-x的后面   
这样找random，往后移一格就ok了，实际上就是让顺序当映射关系了