# 找最优区间(subarray)
别换了马甲就不认识了
# solution
```py
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        costs = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        res = start = curcost = 0
        
        for end in range(len(s)):
            curcost += costs[end]            
            while curcost > maxCost:
                curcost -= costs[start]
                start += 1         
            res = max(res,end-start+1)
            
        return res
```