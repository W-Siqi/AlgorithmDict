basic operation of linked-list  
to be more consise:  
use divmode(,)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = ListNode(0)
        cur = res
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            carry, fv = divmod(v1 + v2 + carry,10)
            """"
            OR we NEED to wirte like this:
            if s > 9:
                newnode.val = s - 10
                carry = 1
            else:
                newnode.val = s
                carry = 0
            """
            cur.next = ListNode(fv)
            cur = cur.next
        
        return res.next
                
``` 