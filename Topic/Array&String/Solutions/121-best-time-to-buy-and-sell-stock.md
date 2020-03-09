```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        earn = 0
        curMin = prices[0]
        for p in prices:
            curMin = min(p,curMin)
            earn = max(earn, p - curMin)
            
        return earn
```