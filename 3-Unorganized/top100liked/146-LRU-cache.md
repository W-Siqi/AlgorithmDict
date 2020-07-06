# hash定位，链表维护优先级
查询用hash 没错，就是移除cache需要维护一个队列。   
- 队列如果是链表，那么提前的操作就是O(1  
## hash 存的是链表的指针
这样就可以吧hash和队列关联起来

# 手撸双向list+hash
```c++
class Node{
public:
    int key;
    int value;
    Node* pre;
    Node* next;
    
    Node(int key,int value){
        this->key = key;
        this->value = value;
        pre = nullptr;
        next = nullptr;
    }
};
class LRUCache {
private:
    int capacity;
    unordered_map<int,Node*> mp;
    Node* tail;
    Node* head; 
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if(mp.count(key)){
            setToHead(mp[key]);
            return mp[key]->value;
        }
        else{
            return -1;
        }
    }
    
    void put(int key, int value) {
        if(mp.count(key)){
            // set value
            mp[key]->value = value;
            // set to head
            setToHead(mp[key]);
        }
        else{
            // not exist
            auto newNode =  new Node(key,value);
            mp[key] = newNode;
            if(mp.size() == 1){
                tail = head = newNode;   
            }
            else if(mp.size() <= capacity){
                newNode->next = head;
                head->pre = newNode;
                head = newNode;
            }
            else{
                newNode->next = head;
                head->pre = newNode;
                head = newNode;
                
                // remove tail
                mp.erase(tail->key);
                tail = tail->pre;
                delete(tail->next);
                tail->next = nullptr;
            }
        }    
    }
    
    void setToHead(Node* node){
        if(node == head){
            return;
        }
        node->pre->next = node->next;
        if(node != tail){
            node->next->pre = node->pre;
        }
        else{
            tail = node->pre;
        }
        node->next = head;
        node->pre = nullptr;
        head->pre = node;
        head = node;
    }
};

```