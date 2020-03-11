
https://www.runoob.com/python3/python3-func-enumerate.html
# cheating code
```py
# binary search
bisect.bisect_left(array, target)
```
# tuple
```python
tup1 = (1, 2, "siqi", 4, 5 )
tup2 = "a", "b", "c", "d"   # even don't need ()
```
# sort
```python
# list.sort( key=None, reverse=False)
# use attrgetter(name)
from operator import attrgetter
sorted_list = sorted(sorted_list, key=attrgetter('val'))
```

sorted
```py
## sort the string will become list!
a = "bca"
b = sorted(a)
print(b) # out put ['a','b','c']
```

# if 
```python
# return val in if 
if obj
if list
if ...
```

# for
### range()
```python
# traverse with index
for i in range(len(a)))：
    print a[1]

# traverse with element
for char in testStr:
    print char
```

### enumerate()
```python
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']

>>>list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

>>>list(enumerate(seasons, start=1)) 
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```
# obj
a = copy.deepcopy(b)

# useful operaters
```python
x =  a if ...  else b
```
```python
print(10//3) # output: 3
print(10%3) # output: 1
```

# dict
``` python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict[Name] # output: 'Zara'
dict[Name] = 'new name' # modify the value

# delete this item
del dict['Name'] 

# clear the dict
dict.clear() 

# if has the key..
if 'Name' in dict:
    print "the key 'Name' is in the dictionary"

# list can not be key, convert it to tuple!
li = [1,213,5,43]
dict[tuple(li)] = []
```

# useful functions
## enumerate() 
```python
for i,num in enumerate(nums):
    print('index:',i,'element:',num)
```
## divmode( , )
```python
x = divmod(27, 10)
print(x) # x = (2,7)
```
# list
```py
# last val
>>> some_list = [1, 2, 3]
>>> some_list[-1] = 5 # Set the last element
>>> some_list[-2] = 3 # Set the second to last element
>>> some_list
[1, 3, 5]

#### list.sort()
#### list.append(obj)
#### list.pop()   
remove the last obj # the return value is the obj
#### list.pop(index) 
the return value is the obj
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.reverse()
```

```py
# create grid d[m][n]
dp = [[0 for a in range(n)] for a in range(m)]
# !DONT USE THIS:
# it seems it copied by reference, not values 
dp = m*[[0]*n]
```
# math
```python
# div mod
>>> divmod(7, 2)
(3, 1)
>>> divmod(8, 2)
(4, 0)
>>> divmod(8, -2)
(-4, 0)
>>> divmod(3, 1.3)
(2.0, 0.3999999999999999)
# pow 
intMax = pow(2,31)-1 
# abs
# infinity
inf = float("inf")
```

# concise writing 
swap
```python
a,b= b,a
```
rank locally
```python
 # rank from i+1 to last
                nums[i+1:len(nums)] = sorted(nums[i+1:len(nums)])
```

build list using 'for if'
```python
# In general
[f(x) if condition else g(x) for x in sequence]
# And, for list comprehensions with if conditions only,

[f(x) for x in sequence if condition]

# an example
heap = [(head.val, i, head) for i,head in enumerate(lists) if head]
```

# Others
## heap
https://docs.python.org/zh-cn/3/library/heapq.html
## type convert
```py
# chars[] to string:
s = ''.join(chars)

# int to char

# char to int
```
## local function
local function can use the parameter of its parent function.  
no sometimes no need to pass it every time