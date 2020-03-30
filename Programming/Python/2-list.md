# create
```py
# empty
li = []

# with inicial element
li = [1,2,"can_be_str"]

# use "for"
li1 = [1,2,3,4,5,7]
li2 = [x for x in li2 if x > 3]
li2 = [x + 1 for x in li2 if x > 3]
# or another way...
[f(x) if condition else g(x) for x in sequence]
```

# access
```py

# last element 
li[-1] 

# from the first to index 4(excluded)
li[:4]

# from the index 2(included) to the last value
li[2:]

# from index 2(included) to 5(excluded)
li[2:5]

# all element
li[:]
```

# query
```py
# if ... exist
if "can-do" in altitude:
    print("good")

# check if empty list
if not li:
    pass

# get index
fruits.index("cherry")

# get count of element
fruits.count("cherry")
```

# add element
```py
# add to the last
li.append("tail")

# insert at specifc index 
# the index element == i , after the execution 
li.insert(i, "new element")
```

# remove element
```py
# pop the last val
lastVal = li.pop()
# pop at given index
element = li.pop(0)

# clear...
li.clear()

# remove() (only remove the first element of given value!!)
li.remove("the element want to remove")

# del by index
del li[0]
# del by selecting an area
del li[:3]

```

# copy
```py
# use copy()
newLi = li.copy()

# use list
newLi = list(li)
```

# join
```py
# ust +
li3 = li1 + li2

# use extend (add whole list to the tail of another)
li1.extend(li2)
```

# reverse
```py
# reverse the elements in place
li.reverse()
```