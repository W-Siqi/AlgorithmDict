# 定长slding window找最优值
```py
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        oldsum = 0
        for i in range(len(customers)):
            oldsum += customers[i]*(1-grumpy[i])
            
        maxSave = curSave = 0
        for i in range(len(customers)):
            curSave += customers[i]*grumpy[i]
            if i >= X:
                curSave -= customers[i-X]*grumpy[i-X]
            maxSave = max(maxSave,curSave)
        return oldsum + maxSave
```