# 寻找最优subarray
- solution1 老老实实的sliding window
- solution2 通过记录下标的方式，更激进的去排除
# solution 1
出错bug：
1. k == 0的egde case
2. 一开始，我是start一直前进到没有s[start]为止，但最先消失不一定是s[start],如bnb，b开始，最先消失的是n
```py
class Solution(object):   
    def lengthOfLongestSubstringKDistinct(self, s, k):
        seen = collections.defaultdict(int)
        res = start = 0

        for end,char in enumerate(s):
            seen[char]+=1

            if len(seen) > k:
                while start <= end:
                    seen[s[start]]-=1
                    if seen[s[start]] == 0: 
                        del seen[s[start]]
                    start += 1
                    if len(seen) <= k: 
                        break

            res = max(res,end-start+1) 
        return res   
```

# solution2 更激进的排除法
```py
class Solution(object):  
    def lengthOfLongestSubstringKDistinct(self, s, k):
        seen = collections.defaultdict(int)
        res = start = 0
        for end,char in enumerate(s):
            seen[char] = end
            if len(seen) > k:
                key,val = min(seen.items(),key = lambda x:x[1])
                start = val + 1
                del seen[key]
            res = max(res,end-start+1) 
        return res
```