# hash + graph 
最暴力的，就是对于每个query，去搜索路径，看看有没有经过一些点。  
## 第一层优化，频繁查询用hash把结果bake一下
after[presequie] = [course1,cours2,....]  
这样只要查一下就行了。  
意识到list可能会很长，把list换成set也一样   
after[presequie] = set(course1,cours2,....)  

但是超时了
## 第二波优化：类似Dijkstra
前面超时，是因为构建hash的时候，同一个路径会遍历多次，如a->b->c->d->e， 从a出发，b出发，c出发都会遍历，这样算法复杂爆炸。    

然后我就想到了Dijksra搭桥的那种感觉，  
每引入新的边 start->end：
- 所有以start结尾的，都是end的prerequisite，以end结尾的，同时都有他们
- 所有end后面的course，start也是他的prerequisite，以course结尾的，也都有start

## Floyd-Warshall？
我看disscuss 里面有个这个算法和我的有点类似？


# TLE solution
```py
class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        req = set()
        graph = collections.defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])
            
        for i in range(n):
            # add prequisitse start from i
            stack = []+graph[i]
            while stack:
                top = stack.pop()
                req.add(str(i)+'-'+str(top))
                if top in graph:
                    for course in graph[top]:
                        stack.append(course)
        res = []
        for q in queries:
            if str(q[0])+'-'+str(q[1]) in req:
                res.append(True)
            else:
                res.append(False)
        return res
``` 
# AC solution
```py
class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        req = collections.defaultdict(set)      
        end = collections.defaultdict(set)
        for p in prerequisites:
            req[p[0]].add(p[1])
            end[p[1]].add(p[0])
            for course in end[p[0]]:
                req[course].add(p[1])
                end[p[1]].add(course)
            for course in req[p[1]]:
                req[p[0]].add(course)
                end[course].add(p[0])
        res = []
        for q in queries:
            if q[1] in req[q[0]]:
                res.append(True)
            else:
                res.append(False)
        return res
```