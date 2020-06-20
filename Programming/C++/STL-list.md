# List 创建
```c++
list<int>a{1,2,3}
list<int>a(n)    //声明一个n个元素的列表，每个元素都是0
list<int>a(n, m)  //声明一个n个元素的列表，每个元素都是m
list<int>a(first, last)  //声明一个列表，其元素的初始值来源于由区间所指定的序列中的元素，first和last是迭代器
```
# 插入
```c++
a.push_front()//头部插入
a.push_back()//尾部插入
a.insert(a.begin(),100);  //在a的开始位置（即头部）插入100
a.insert(a.begin(),2, 100);   //在a的开始位置插入2个100
a.insert(a.begin(),b.begin(), b.end());//在a的开始位置插入b从开始到结束的所有位置的元素
```

# 删除
```c++
a.clear( ) // 清空
a.pop_front( )// 删除头部元素（注意不能为空）
a.pop_back( )// 删除尾部元素（注意不能为空）

a.remove(n);//删除所有值为n的元素
a.erase(a.begin());// 删除指定位置的元素
a.erase(a.begin(),a.end());// 删除给定区间的元素
```