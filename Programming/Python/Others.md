# about value passing 
list and dict are passed by reference(both as argument and variable)
```py
li1 = []
li2 = li1 # li2 is the reference of li1 
li3 = li1.copy()  # if we want to pass by value...
dosomething(li) # passed by reference
```

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

# if 
```python
# return val in if 
if obj
if list
if ...
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

# useful functions
## divmode( , )
```python
x = divmod(27, 10)
print(x) # x = (2,7)
```
# list
#### list.sort()

# concise writing 
swap
```python
a,b= b,a
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