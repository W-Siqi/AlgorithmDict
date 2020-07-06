# 维护最值 --> 使用priority queue！
我的solution 2，用vector+二分，始终维护顺序。   
但时vector的insert操作是很昂贵。   
这里priority_queue是完爆的，因为不但树的操作没那么贵，而且红黑树不用每次插入都调整。
# 被遗忘的O(N)
分析复杂度的话，solution2是O(lgN*M) solution1 是O(lgN * N) (M <= N)  
但solution2 每次更新有个vector.insert() 这是一个O(N)的操作。  
有时候忘记了数据结构的操作，solution2看似比solution1优，但是solution1跑起来比solution2快7倍。
# solution 1
直接全弹出来进行排序
```c++
class Solution {
public:
    static bool compare(ListNode* n1,ListNode* n2){
        if(n1 == nullptr || n2 == nullptr){
            return n1 == nullptr;
        }
     
        return n1->val < n2->val;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<ListNode*> nodes;
        for(auto li:lists){
            ListNode* p = li;
            while(p){
                nodes.push_back(p);
                p = p->next;
            }
        }
        
        sort(nodes.begin(),nodes.end(),compare);
        
        if(nodes.size() == 0){
            return nullptr;
        }
        
        for(int i = 0; i < nodes.size()-1; i++){
            nodes[i]->next = nodes[i+1];
        }
        nodes[nodes.size()-1]->next = nullptr;
        
        return nodes[0];
    }
};
```

# solution 2
vector + 二分查找
```c++
class Solution {
public:
    static bool compare(ListNode* n1,ListNode* n2){
        if(n1 == nullptr || n2 == nullptr){
            return n1 == nullptr;
        } 
        return n1->val < n2->val;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        sort(lists.begin(),lists.end(),compare);
        vector<ListNode*> nodes;
        
        while(lists.size() > 0){
            if(lists[0] == nullptr){
                lists.erase(lists.begin());
                continue;    
            }
            
            nodes.push_back(lists[0]);
            lists[0] = lists[0]->next;
            ListNode* newList = lists[0];          
            lists.erase(lists.begin());         
            if(newList != nullptr){
                int l = 0, r = lists.size();
                while(l<r){
                    int mid = l + (r-l)/2;
                    if(lists[mid]->val < newList->val){
                        l = mid + 1;
                    }
                    else{
                        r = mid;
                    }
                }
                lists.insert(lists.begin()+r,newList);
            }
        }
        
        if(nodes.size() == 0){
            return nullptr;
        }
        
        for(int i = 0; i < nodes.size()-1; i++){
            nodes[i]->next = nodes[i+1];
        }
        nodes[nodes.size()-1]->next = nullptr;
        
        return nodes[0];
    }
};
```