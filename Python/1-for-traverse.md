```py
# use range
for i in range(len(arr)):
    print(arr[i])

for i in range(2,6):
    print(i) # output: 2,3,4,5

for i in range(3, 12, 3):
    print(i) # output: 3,6,9


# iterare element 
for element in arr:
    print(element)


# use enumerate
for i, e in enumerate(arr):
    print("index",i)
    print("element",e)

for i, e in enumerate(arr, start = 2):
    print("index",i)
    print("element",e)


# traverse list<"vector">
for x,y in si:
    print("list[0]",x)
    print("list[1]",y)
```
