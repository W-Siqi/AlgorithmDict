# Dangersous things
### when remove the element of the list
be sure havn't store the i as the "ointer"  
be sure the enmurator works well in the continuing loop
### when insert a val in decreasing order:
```python         
    place = 0
    while place < len(heads) and heads[place].val <= top.next.val:
        place+=1
    heads.insert(place,top.next)
```

### when forget to update the dynamic flag varibles 
https://leetcode.com/submissions/detail/297418896/

## miss the case when quit while loop
```py
# for example, after the operation2, it will quit the loop, but if the code rely on operation 1 to do (such as update the reasut), it will miss this case.
while condition:
    operation1
    operation2
```
#### to avoid this, we can think about how to write code in loop

## forget the return value in python
something horiible will happen...

# Edge cases
### two sum
[1,3,4,5,6,7] and target = 6 : cannot use 3 + 3 = 6  
be careful about the duplication!

### median of two sumed arrays
https://leetcode.com/submissions/detail/295159044/  
while a < b => while a <= b  
lession here: the <= and < in while loop control is important. because if you use the wrong one , there must exist a edge case to make your index out of range

### the []
https://leetcode.com/submissions/detail/297329660/
if easiest way is to use 'if' in the first place
