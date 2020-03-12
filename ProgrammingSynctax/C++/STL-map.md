# Map<key,value>
```c++
// 创建一个<key,value>型的map
map<int,int> m;

// 元素个数
m.size()

// 赋值/创建, 如果key值有就覆盖，没有就创建
m[k] = val;

// 查询key值是否存在
if(m.count(key)>0){ 
    ...;
}

if(m.find(key) != m.end()){
    ....;
}

// 遍历
for(auto iter = m.beign(); iter != m.end(); iter++){
    cout<<"key: "<<iter->first;
    cout<<"value: "<<iter->second; 
}

// 删除
m.earse(key);
```

# unordered_map<key,value>
almost the same behaviour with map, just different implementation

# set<value>
```c++
// 创建
set<int> s;

// 插入
s.insert(1);
s.insert(2);

// 删除
s.erase(1);

// 查询
if(s.find(2) != s.end()){
    cout<< "2 is in the set";
}
```