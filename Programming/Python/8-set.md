# 创建
```py
# 方法1，set()
s = set()

# 方法2，{...}
# 因为dict也是用{}, 所以空集合必须用set()，不然就混淆了
s = {'a','e','i','o','u'}

# 方法3, 集合推导式，和list很像
a = {x for x in 'abracadabra' if x not in 'abc'}

```
Q:集合能包含重复的元素吗？

# 基本操作
```py
# 添加
s.add('a')
# 删除
s.discard('a')
s.remove('a') # 不推荐用remove，如果被移除的元素本身就不在的话，会出错
# 查询
if 'a' in s:
    pass
```

# 其他常见操作  
### len(s) 返回元素个数
### intersection() 交集
### union() 并集