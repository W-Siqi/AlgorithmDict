# subarray 是否存在问题
solution2：这题更特殊的是，他是一个定长的slding window
# solution 1
比较标准的slding window，  
这种题目核心的地方往往就是：
1. 你怎么设计数据结构追踪当前window
2. 如何根据window的数据重置start，end两个指针的位置
```py
class Solution(object):
    def checkInclusion(self, s1, s2):
        needs = collections.Counter(s1)
        window = collections.Counter()        
        
        valid = 0
        for end,char in enumerate(s2):
            head = end - len(s1)
            if head >= 0 and s2[head] in needs:
                window[s2[head]] -= 1
                if window[s2[head]] < needs[s2[head]]:
                    valid -= 1
            if s2[end] in needs:
                window[s2[end]] += 1
                if window[s2[end]] <= needs[s2[end]]:
                    valid += 1
            if valid == len(s1):
                return True
        return False
```
# solution 2 利用定长的slding window
就是维护一个k长度的window划过去，是O(N)
但是比较的时候，拿整个tuple或者dict去比较复杂度是O(k)的？  
虽然写上去简单，似乎时间效率不如solution1.