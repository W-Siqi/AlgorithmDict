# hash名场面
这题竟然可以做到O（n）   
因为这题有一个很好免重复遍历sequence的方法，就是只从sequence开始开始数。   
而妙的地方，在于，对于num，只要看num-1在不在set里，就可以知道他重复不重复了。
# solution
```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> seen;
        for(int num:nums){
            seen.insert(num);
        }
        int res = 0;
        for(auto it = seen.begin(); it != seen.end();it++){
            if(!seen.count(*it-1)){
                int len = 1;
                int forward = *it+1;
                while(seen.count(forward)){
                    len++;
                    forward++;
                }
                res = max(res,len);
            }
        }
        return res;
    }
};
```