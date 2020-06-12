# 寻找最优subarray
第一写遇到的BUG：  
通过存下标来快速重置start指针，  
但是重置的时候，忘记维护seen里面的数据了。
# solution
```py
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = collections.defaultdict(int)
        start = res = 0
        for end,char in enumerate(s):
            if char in seen:
                for i in range(start,seen[char]):
                    if seen[s[i]] < seen[char]+1:
                        del seen[s[i]]
                start = seen[char]+1       
            seen[char] = end
            res = max(res,end-start+1)
        return res
```