# 这题，就是发现贪心策略： 只要有涨幅差，我就买卖。
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,cur = 0,0
        while cur < len(prices):
            sell = cur
            while sell + 1 < len(prices) and prices[sell+1] >= prices[sell]:
                sell += 1
            profit += (prices[sell] - prices[cur])
            cur = sell + 1
        return profit
        
```