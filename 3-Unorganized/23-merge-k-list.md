# soluton1: time exceed, find the smallest each time.  
the wrostst case: [[1][2][3][4].....[9999999]] will use O(n^2)
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = []
        res = tail = ListNode(0)
        for li in lists:
            heads.append(li)
        
        while(True):
            winner = -1
            smallest = float("inf")
            for i in range(len(heads)):
                if heads[i] == None:
                    continue
                if heads[i].val < smallest:
                    winner = i
                    smallest = heads[i].val

            if winner == -1:
                # no elements anymore
                break
            else:
                # add the biggest value
                tail.next = ListNode(heads[winner].val)
                tail = tail.next
                heads[winner] = heads[winner].next
        
        return res.next
```

# solution2: optmized soluton 1
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = []
        res = tail = ListNode(0)
        for li in lists:
            heads.append(li)
        
        while(True):
            winner = -1
            smallest = float("inf")
            for i in range(len(heads)):
                if heads[i] == None:
                    continue
                if heads[i].val < smallest:
                    winner = i
                    smallest = heads[i].val

            if winner == -1:
                # no elements anymore
                break
            else:
                # add the biggest value
                tail.next = ListNode(heads[winner].val)
                tail = tail.next
                if heads[winner].next != None:
                    heads[winner] = heads[winner].next
                else:
                    # optimize: remove empty
                    del heads[winner]
                
                
        
        return res.next
```

# solution3: build big vision first
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        allnodes = []
        for head in lists:
            while head is not None:
                allnodes.append(head)
                head = head.next
        
        from operator import attrgetter       
        allnodes.sort(key=attrgetter('val'))
        
        dummyhead = tail = ListNode(0)
        for node in allnodes:
            tail.next = ListNode(node.val)
            tail = tail.next
        
        return dummyhead.next
```

# solution4: heap style
  
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = [node for node in lists if node]
        
        from operator import attrgetter       
        heads.sort(key=attrgetter('val'))
        
        dummy = tail =ListNode(0)
        while heads:
            top = heads.pop(0)
            # get first val
            tail.next = ListNode(top.val)
            tail = tail.next
            
            # replace 
            if top.next is not None:
                place = 0
                while place < len(heads) and heads[place].val <= top.next.val:
                    place+=1
                heads.insert(place,top.next)
        
        return dummy.next
```