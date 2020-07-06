# 缓存遍历结果
就是min每次替换的时候，把老的min塞进去。  
这样就是退回来的时候，不用重遍历，用这个老的就ok了
# solution 1 直接缓存结果
```c++
class MinStack {
private:
    stack<int> s;
    int min;
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        if(s.size() == 0 || x <= min){
            // if min changed, store the old min in the stack
            s.push(min);
            min = x; 
        }
        s.push(x);
    }
    
    void pop() {
        if(s.top() == min){
            // if min change, we have stored the old min in the stack, just get it , no need to traverse again 
            s.pop();
            min = s.top();
            s.pop();
        }
        else{
            s.pop();
        }
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return min;
    }
};
```

# solution 2 把结果bake到element上面
就是每次的老min value 会占stack的空间。  
一个优化方法，就是value存的是和**当前**min的差值：
- 知道当前min，可以还原之前的元素
- 如果，差值<0,说明是min的切换点（比之前的min要小嘛）。所以还原之前的min，就是减去这个为负数的差值