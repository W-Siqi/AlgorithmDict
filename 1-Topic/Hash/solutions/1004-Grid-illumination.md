# takeaway
- 这里用hash的motivation还是，用来当计分板，检索查询。
- 这里的简单数学，在同直线上的点，他们在x,y上的截距相等，因为这里的斜率又是定死的，所以截距相等，那么就是在diagonal上了

# solution(stupid version)
这个写法很傻逼，大量雷同结构代码，不但繁琐，而且会引入bug
```py
class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        crossx,crossy,x_align,y_align = {},{},{},{}
        lampCoords = set()
        for lamp in lamps:
            x,y = lamp[0],lamp[1]
            lampCoord = (x,y)
            lampCoords.add(lampCoord)
            if x in x_align: x_align[x].append(lampCoord)
            else: x_align[x] = [lampCoord]
            
            if y in y_align: y_align[y].append(lampCoord)
            else: y_align[y] = [lampCoord]
        
            cx,cy  = x - y, x + y
            if cx in crossx: crossx[cx].append(lampCoord)
            else: crossx[cx] = [lampCoord]
            if cy in crossy: crossy[cy].append(lampCoord)
            else: crossy[cy] = [lampCoord]
        
        res = []
        for q in queries:
            x,y = q[0],q[1]
            cx,cy = x-y,x+y
            if x in x_align or y in y_align or cx in crossx or cy in crossy:
                res.append(1)
            else:
                res.append(0)
                
            offsets = [(0,0),(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]
            delLamps = [(x+f[0],y+f[1]) for f in offsets if (x+f[0],y+f[1]) in lampCoords]
            for lampCoord in delLamps:
                x,y = lampCoord[0],lampCoord[1]
                cx,cy = x-y,x+y
                if x in x_align and lampCoord in x_align[x]:
                    x_align[x].remove(lampCoord)
                    if len(x_align[x]) == 0: del x_align[x]
                if y in y_align and lampCoord in y_align[y]:
                    y_align[y].remove(lampCoord)
                    if len(y_align[y]) == 0: del y_align[y]
                if cx in crossx and lampCoord in crossx[cx]:
                    crossx[cx].remove(lampCoord)
                    if len(crossx[cx]) == 0: del crossx[cx]
                if cy in crossy and lampCoord in crossy[cy]:
                    crossy[cy].remove(lampCoord)
                    if len(crossy[cy]) == 0: del crossy[cy]
        return res
```
# solution(使用for loop 简化)
```py
class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        illuDicts = [{},{},{},{}]
        lampCoords = set()
        for lamp in lamps:
            x,y = lamp[0],lamp[1]
            lampCoord = (x,y)
            lampCoords.add(lampCoord)
            illuKeys = (x,y,x-y,x+y)
            
            for i in range(4):
                k,d = illuKeys[i], illuDicts[i]
                if k not in d: d[k] = []
                d[k].append(lampCoord)
                
        res = []
        for q in queries:
            # look up
            illuKeys = (q[0],q[1],q[0]-q[1],q[0]+q[1])
            qres = 0
            for i in range(4):
                if illuKeys[i] in illuDicts[i]: qres = 1
            res.append(qres)
            
            # remove
            offsets = [(0,0),(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]
            delLamps = [(q[0]+f[0],q[1]+f[1]) for f in offsets if (q[0]+f[0],q[1]+f[1]) in lampCoords]
            for lampCoord in delLamps:
                illuKeys = (lampCoord[0],lampCoord[1],lampCoord[0]-lampCoord[1],lampCoord[0]+lampCoord[1])
                for i in range(4):
                    k,d  = illuKeys[i],illuDicts[i]
                    if k in d and lampCoord in d[k]:
                        d[k].remove(lampCoord)
                        if len(d[k]) == 0: del d[k]
        return res
```

# solution2
基本思路是一样的，就是dict没有必要存具体坐标，只要存计数就行了。  
我们在保证只会删一次的情况下，遇见lamp，只要counter--就ok了
```py
class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        illuDicts = [collections.Counter(),collections.Counter(),collections.Counter(),collections.Counter()]
        lampCoords = set()
        for lamp in lamps:
            x,y = lamp[0],lamp[1]
            lampCoords.add((x,y))
            illuKeys = (x,y,x-y,x+y)        
            for i in range(4):
                illuDicts[i][illuKeys[i]] += 1
                
        res = []
        for q in queries:
            # look up
            illuKeys = (q[0],q[1],q[0]-q[1],q[0]+q[1])
            qres = 0
            for i in range(4):
                if illuDicts[i][illuKeys[i]] > 0: qres = 1
            res.append(qres)
            
            # remove
            offsets = [(0,0),(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]
            delLamps = [(q[0]+f[0],q[1]+f[1]) for f in offsets if (q[0]+f[0],q[1]+f[1]) in lampCoords]
            for lampCoord in delLamps:
                lampCoords.remove(lampCoord)
                illuKeys = (lampCoord[0],lampCoord[1],lampCoord[0]-lampCoord[1],lampCoord[0]+lampCoord[1])
                for i in range(4):
                    illuDicts[i][illuKeys[i]]-=1
        return res
```