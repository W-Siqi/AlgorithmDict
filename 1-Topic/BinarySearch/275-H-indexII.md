# Mark： 二分 try strtagy 的编程模型
# solution 1 - BS
这个写法太啰嗦了，简化一哈！
```py
# 注意二分lo=mid这种死循环
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo,hi = 0, len(citations)
        
        if hi == 0:
            return 0
        elif hi == 1:
            return 1 if citations[0] > 0 else 0
        
        # 注意这里讨论edge case的写法，通过pass test的模型，来讨论分支
        def isIndex(citations,index):
            if index > 0 and citations[-index] < index:
                return False
            if index < len(citations) and citations[-index - 1] > index:
                return False
            return True
        
        # edge case: hi = len
        while lo < hi:
            mid = (lo+hi)//2
            # try mid as index
            lowerBound,upperBound = citations[-mid-1],citations[-mid]
            h = mid
            if lowerBound > h:
                # too small
                lo = mid + 1
            elif upperBound < h:
                # too big
                hi = mid - 1
            else:
                # is a ok option: lowerBound <= h and upperBound >= h
                # try bigger
                if mid > lo:
                    lo = mid
                else:
                    # only two left
                    if isIndex(citations,hi):
                        return hi
                    else:
                        return lo
        return lo

```

# solution 2
另一种思考方式，随着h越来越大, upperbound,citation[-h]越来越小。  
其实没有必要考虑lowerBound， upperBound**有潜力**就往前推。  
所以是一个找upperBound 的 问题？？？？