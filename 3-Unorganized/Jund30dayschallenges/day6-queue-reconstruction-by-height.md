# Greedy

```py
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x:x[1])
        res = []
        for p in people:
            count = i = 0
            while i < len(res):
                if res[i][0] >= p[0]:
                    count += 1
                if count > p[1]:
                    break
                else:
                    i += 1
                # print(i,count)
            res.insert(i,p)
            # print(i,res)
        return res
```