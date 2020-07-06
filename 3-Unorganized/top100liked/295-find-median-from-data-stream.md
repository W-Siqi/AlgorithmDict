# 维护次序：heap
- 不要想着用vector维护次序，vector插入删除是O（N）
- but， heap无法随时知道全排列的状况
- but，这题不需要知道全排列
## two-heap算法
中位数左边维护大顶堆，右边维护小顶堆...
```c++
class MedianFinder {
private:
    priority_queue<int,vector<int>,less<int>> font;
    priority_queue<int,vector<int>,greater<int>> back;
public:
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        // ensure font small and back big
        if(font.size() == 0 || num <= font.top()){
            font.push(num);
        }
        else{
            back.push(num);
        }
        
        // ensure number euqal
        while(font.size() < back.size()){
            font.push(back.top());
            back.pop();
        }
        
        while(back.size() + 1 < font.size()){
            back.push(font.top());
            font.pop();
        }
    }
    
    double findMedian() {
        if(font.size()==back.size()){
            return font.size() == 0?0:(double)(font.top()+back.top())/2;
        }
        else{
            return (double)font.top();
        }
    }
};
```