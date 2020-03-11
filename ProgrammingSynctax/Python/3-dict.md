# create
``` py
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict[Name] # output: 'Zara'
dict[Name] = 'new name' # modify the value

# list can not be key, convert it to tuple!
li = [1,213,5,43]
dict[tuple(li)] = []
```

# traverse
```py
for k in dict.keys():
    pass

for v in dict.values():
    pass
    
for k,v dict.items():
    pass
```

# delete & add
```py
# delete this item
del dict['Name'] 

# clear the dict
dict.clear() 
```

# query
```py
# if has the key..
if 'Name' in dict:
    print "the key 'Name' is in the dictionary"

# len
len(dict)
```