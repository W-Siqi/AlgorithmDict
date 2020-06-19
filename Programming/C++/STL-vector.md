
# vector
### 创建 vector
```c++
// 列表初始化
vector<int> a{1,2,3,4,5};

// 定义了10个整型元素的向量
// 但没有给出初值，其值是不确定的。
vector<int> a(10); 

// 定义了10个整型元素的向量,且给出每个元素的初值为1
vector<int> a(10,1); 

//用b向量来创建a向量，整体复制性赋值
vector<int> a(b); 

//定义了a值为b中第0个到第2个（共3个）元素
vector<int> a(b.begin(),b.begin+3); 

// 从数组中获得初值
int b[7]={1,2,3,4,5,9,8};
vector<int> a(b,b+7); 
```

### 访问元素
```c++
a.back(); //返回a的最后一个元素
a.front(); //返回a的第一个元素
a[i]; //返回a的第i个元素，当且仅当a[i]存在2013-12-07
```

### 访问状态
```c++
a.empty(); //判断a是否为空，空则返回ture,不空则返回false
a.size(); //返回a中元素的个数；
a.capacity(); //返回a在内存中总共可以容纳的元素个数
```

### 插入&删除
```c++
// 末尾插入
a.push_back(5); 
// 删除末尾
a.pop_back(); 

// 插入后5的下标为1 ，如a为1,2,3,4，插入元素后为1,5,2,3,4
a.insert(a.begin()+1,5); 
//清空a中的元素
a.clear(); 

// 删除下标为i的元素
a.erase(a.begin()+i);
// 删除 从下标 i（包括） 到 j（不包括） 的元素
a.erase(a.begin()+i,a.begin()+j); 
```

# 大数据优化：capacity
```c++
// 初始化带capacity：
int capacity=100;
vector<int>  a(capacity);
// 改变现有的capacity
a.reserve(100);
```

其他
.empty() /.size（）/.begin()/.end() 这4个好像所有容器都可以？似乎是基于iterator的？

# algorithm
## 排序（默认升序）
```c
vector<int> GetRanked(vector<int>& src){
        vector<int> dest(src);
        sort(dest.begin(),dest.end());
        return dest;
    }
```
（1）sort(a.begin(),a.end()); //对a中的从a.begin()（包括它）到a.end()（不包括它）的元素进行从小到大排列
（2）reverse(a.begin(),a.end()); //对a中的从a.begin()（包括它）到a.end()（不包括它）的元素倒置，但不排列，如a中元素为1,3,2,4,倒置后为4,2,3,1
（3）copy(a.begin(),a.end(),b.begin()+1); //把a中的从a.begin()（包括它）到a.end()（不包括它）的元素复制到b中，从b.begin()+1的位置（包括它）开        始复制，覆盖掉原有元素
（4）find(a.begin(),a.end(),10); //在a中的从a.begin()（包括它）到a.end()（不包括它）的元素中查找10，若存在返回其在向量中的位置
找最大
