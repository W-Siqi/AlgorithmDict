list.sort(cmp=None, key=None, reverse=False)

# li.sort() and sorted(li)
```py
# sort() will make it inplace 
li.sort()
# sorted() will return the sorted array
sortedLi = sorted(li)

## sort the string will become list!
a = "bca"
b = sorted(a)
print(b) # out put ['a','b','c']
```
# sort reverse
```py
li.sort(reverse = False)
```

# sort with given key
```py
# use the first element as the key
def takeSecond(elem):
    return elem[0]
random.sort(key=takeSecond)
# or just use lambda
si.sort(key=lambda x:x[0])

# rank from i+1 to last
nums[i+1:len(nums)] = sorted(nums[i+1:len(nums)])
```