# hash的motivation
还是个检测冲突的功能，不过这题的重点不是hash。是提取特征

# 提取特征（设计hash值）
这题的核心，对一个shape设计一个hash值，使得同一个行传。
### 首先，一模一样的shape怎么判定？
对坐标排序就行了，如果是一样，那么排序后的结果是一模一样的
### 8个变形的shape如何判定？
直接枚举出8个变形，然后对着8个shape进行排序
### 启示：sort厉害了
sort是一个很好的解决这类“同分异构”的hash值设计问题

# 简洁写法 - 坐标旋转变换
因为island的初始坐标是乱分布的，而我们拿来比较的手，坐标必须是归一化后的。  
这里的一个好的写法是：**先对着（0,0）变换，再归一化**  
对着(0,0)进行翻转和旋转，形状是不变的，但是写法会很简洁：
```py
# 1）总共8个变形，具体哪个是哪个，自己画一下图就ok了
# 2）x,y翻转很好想
# 3）旋转的话，就是CG里面的2D变换，可以用负数或矩阵都可以啦~ 但这里是90度，所以都是x,-x,y,-y一样的很工整
    shapes[0].append((x,y))
    shapes[1].append((x,-y))
    shapes[2].append((-x,y))
    shapes[3].append((-x,-y))
    shapes[4].append((y,x))
    shapes[5].append((y,-x))
    shapes[6].append((-y,x))
    shapes[7].append((-y,-x))
```
然后再平移bbox(minx,miny)到原点就OK了

# 类似的题目
**leetcode - 49-group-nanagrams**
同样，保证有相同特征的，hash值一样
# 发现的一个python常识错误...
[]传递的是引用
```py
# 坑爹的python[[]]*8是吧[]这个引用复制了8遍...
shapes = [[]]*8
# 也就是说shape[0]和shape[1]指向的是同一个东西
```
# solution
```py

class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def findIsland(x,y,il,grid):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0: return 
            il.append([x,y])
            grid[x][y] = 0
            findIsland(x,y-1,il,grid)
            findIsland(x,y+1,il,grid)
            findIsland(x-1,y,il,grid)
            findIsland(x+1,y,il,grid)
    
        
        def normalizeCoord(coords):
            minx,miny = 99999,99999 # max grid N = 50
            for x,y in coords:
                minx = min(minx,x)
                miny = min(miny,y)
            for i in range(len(coords)):
                coords[i] = (coords[i][0]-minx,coords[i][1]-miny)
            coords.sort()
            
        def encode(island):
            shapes = [[],[],[],[],[],[],[],[]]
            for coord in island:
                x,y = coord[0],coord[1]
                shapes[0].append((x,y))
                shapes[1].append((x,-y))
                shapes[2].append((-x,y))
                shapes[3].append((-x,-y))
                shapes[4].append((y,x))
                shapes[5].append((y,-x))
                shapes[6].append((-y,x))
                shapes[7].append((-y,-x))
            for i in range(8):
                normalizeCoord(shapes[i])
            shapes.sort()
            # print("shapes",shapes)
            return tuple(shapes[0])
        
        if not grid or not grid[0]: return 0
        
        islands = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != 0:
                    coords = []
                    findIsland(x,y,coords,grid)
                    # print("island",coords)
                    islands.add(encode(coords))
        return len(islands)
```