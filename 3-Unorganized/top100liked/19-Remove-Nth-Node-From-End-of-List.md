# solution  one pass
一个前一个后，始终保持n的间隔就行了 
```c++
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* first = head; ListNode* after = head; ListNode* pre = nullptr;
        int count = 0;
        while(first){
            first = first->next;
            if(count >= n - 1 && first){
                pre = after;
                after = after->next;
            }
            count += 1;
        }
        
        if(pre == nullptr){
            ListNode* newHead = after->next;
            after->next = nullptr;
            return newHead;
        }
        else{
            pre->next = after->next;
            after->next = nullptr;
            return head;
        }
    }
};
```