# solution 1 - Greedy
```c++
class Solution {
public:
    int jump(vector<int>& nums) {
        int start = 0, end = 1, step = 0;
        while(end < nums.size()){
            int nextEnd = end;
            for(int i = start; i < end; i++){
                nextEnd = max(nextEnd,i+nums[i]+1);
            }
            start = end;
            end = nextEnd;
            step++;
        }
        return step;
    }
};
```