# solution 1 hash
```c++
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_set<ListNode*> seen;
        ListNode* pA = headA;
        while(pA){
            seen.insert(pA);
            pA = pA->next;
        }
        ListNode* pB = headB;
        while(pB){
            if(seen.count(pB)){
                return pB;
            }
            pB = pB->next;
        }
        return nullptr;
    }
};
```

# solution 2, 统计长度再遍历
比如一个len==10,一个len==8  
那么就先让10的那个先跑两步， 然后两个list同步遍历，第一个一样的，就是交叉点
```c++
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* pA = headA;
        int lenA = 0;
        while(pA){
            pA = pA->next;
            lenA++;
        }
        
        ListNode* pB = headB;
        int lenB = 0;
        while(pB){
            pB = pB->next;
            lenB++;
        }
        
        pA = headA;
        pB = headB;
        int maxLen = max(lenA,lenB);
        while(pA && pB){
            if(pA == pB){
                return pA;
            }
            
            if(lenA < maxLen){
                lenA++;
            }
            else{
                pA = pA->next;
            }
            
            if(lenB < maxLen){
                lenB++;
            }
            else{
                pB = pB->next;
            }
        }
        
        return nullptr;
    }
};
```

# solution 3 首尾相接跑循环
listA跑完接listB， B跑完接A。  
这样会相遇在交点，因为此时他们跑了相同的长度，这个画下图就出来了。   
### 就是注意没有交点的时候，要判死循环出来！
```c++
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA == nullptr || headB == nullptr){
            return nullptr;
        }
        ListNode* p1 = headA;
        ListNode* p2 = headB;
        int switchCount = 0;
        while(switchCount < 3){
            if(p1 == p2){
                return p1;
            }
            
            p1 = p1->next;
            p2 = p2->next;
            if(p1 == nullptr){
                p1 = headB;
                switchCount++;
            }
            if(p2 == nullptr){
                p2 = headA;
                switchCount++;
            }
        }
        return nullptr;
    }
};
```