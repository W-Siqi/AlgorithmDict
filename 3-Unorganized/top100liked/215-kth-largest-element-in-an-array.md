
# solution 1, sort, O(N*lgN)
```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end(),[](int a, int b){return a>b;});
        return nums[k-1];
    }
};
```

# solution 2, heap sort, O(N*lgN)
实质上和solution1想法类似，就是排序。   
但是用heap在这种情形比直接全排序要方便：
- 题目不要时刻访问全排序，所以heap足够
- heap很适合数据经常插入删除变动的情形，如果用vector排的话，vector的插入和删除代价是很大的，直接在复杂乘一个O(N),而heap调整的代价相对小很多！
- 总结：priority_queue的情形，就用priority_queue吧~
```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> pq;
        for(int num:nums){
            pq.push(num);
        }
        for(int i = 0; i < k-1;i++){
            pq.pop();
        }
        return pq.top();
    }
};
```
# solution 3 ,heap排行榜, O(N*lgK)
inituaion，就是弄一个当前前k名的排行榜。   
因为top要快速知道排末尾的，所以是小顶堆。
```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int,vector<int>,greater<int>> pq;
        for(int num:nums){
            if(pq.size() < k){
                pq.push(num);   
            }
            else if(num > pq.top()){
                pq.pop();
                pq.push(num);
            }
        }
        return pq.top();
    }
};
```
# solution 4, quick select, O(N)~ O(N*N)
- 首先，要知道为什么另一半不去排，能把O(N*lgN)复杂度变成 O(N)     
因为如果只有一半要partition，就是N+N/2+N/4....是个等比数列，加起来不超过2N，所以就是O(N)
- 其次，什么情况下变成O(N*N)?   
和快排一样，每次都是把N分成1和N-1两半..
## (PS.这个快排的partition复习一下，有些细节没考虑清楚要出错的！)
```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int start = 0, end = nums.size();
        while(start < end){
            int mid = partition(nums,start,end);
            //std::cout<< mid << ", "<<nums[mid]<<std::endl;
            if(mid == k - 1){
                return nums[mid];   
            }
            else if(mid > k - 1){
                end = mid;
            }
            else{
                start = mid + 1;
            }
        }
        return nums[start];
    }
    
    int partition(vector<int>& nums, int start, int end){
        int pivot = nums[start];
        int l = start, r = end - 1;
        while(l < r){
            // 移动pivot的对立面
            while(l < r && nums[r] <= pivot){
                r--;
            }
            // 一定要检测，是因为碰到对面的“奸细”break的才交换，因为若是碰到l指针，交换会导致l > r了！
            if(l<r){
                nums[l++] = nums[r];   
            }
            
            // 重复一遍
            while(l < r && nums[l] > pivot){
                l++;     
            }          
            if(l<r){
                nums[r--] = nums[l];   
            }
        }
        nums[l] = pivot;
        return l;
    }
};
```