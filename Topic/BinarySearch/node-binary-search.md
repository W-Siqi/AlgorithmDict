# case1: find element
```py
def binarySearch(arr,target):
    if not arr:
        reutrn False
    
    low, high = 0, len(arr) - 1
    while(low < high):
        # dont use mid = (low + high)/2 , it will overflow in C++ and Java
        mid = low + (high - low)//2  
        if arr[mid] <  target:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return True

    return True if arr[low] == target else False
```

# case2.1 - find closest(lower bound) 
## remember: 
怎么记住？ 让mid最后落在low， 然后high靠过来（high = mid）
**edge case:** target is vary big, will end with arr[-1] < target
```py
    mid = low + (high - low)//2 
    if arr[mid] <  target:
        low = mid + 1 
    else:
        high = mid
```

# case2.2 - find closest(upper bound) 
怎么记住？ 让mid最后落在high， 然后low靠过来（low = mid）
**edge case:** target is vary small, will end with arr[0] > target
```py
    mid = low + (high - low + 1)//2 
    if target < arr[mid]:
        high = mid - 1 
    else:
        low = mid
```
  
    

# case3.1 - find closest bigger
```py
    if arr[mid] <=  target: # if equal, move towards big
        low = mid + 1 
    else:
        high = mid - 1
```

# case3.2 - find closest smaller
```py
    if arr[mid] <  target:
        low = mid + 1 
    else: # if equal, move towards small
        high = mid - 1
```

