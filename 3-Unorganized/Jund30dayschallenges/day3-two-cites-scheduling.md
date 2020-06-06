# Greedy
这题贪心法的直觉性很强。  
也就是痕迹很明显，找最优方案。  
但是greedy最大难处，是证明...  
就像这题，我做出来了，但是不知道这个是不是最优解
```py
class Solution(object):
    def twoCitySchedCost(self, costs):
        N = len(costs)/2
        costs.sort(key = lambda x:-abs(x[0]-x[1]))
        a = b = cost_sum = 0
        for cost in costs:
            if (cost[0] < cost[1] and a < N) or b >= N:
                cost_sum += cost[0]
                a += 1
            else:
                cost_sum += cost[1]
                b += 1
        return cost_sum
```