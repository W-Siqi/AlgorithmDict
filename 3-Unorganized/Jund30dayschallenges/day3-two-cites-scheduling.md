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