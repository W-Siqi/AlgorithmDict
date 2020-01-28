# different ways to bs

# left&right binary search
1. pointer means include
2. when loop end, right < left
3. must exclude mid, or it will in the dead loop
3. the final pos is right or left depend
4. the final pos **could be out of index?**, if there is no target number larger/smaller every number in array
## when target not found 
### target is larger/smaller than everyone
end = len(a) - 1  
start = len(a)  
or
end = -1
start = 0
## target is between max and min
is between a[end] and a[start]

## when duplication element
# search for closest

