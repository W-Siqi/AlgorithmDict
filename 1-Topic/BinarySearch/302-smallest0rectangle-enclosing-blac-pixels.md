# key& tag
这题的BS，动机和try趋势有点像。  
他们的实质是在试探连续区间， 如00000000000011111111111111000000000  
只是try趋势的题目的，区间是000000000011111111111 或 11111111111110000000000

# py 简洁写法 - any 和 all：
这里的checkRow， 是常见的判断逻辑，其实是可以简洁的
```py
    # 傻瓜原版
    def checkRow(image,row):
        hasOne = False
        for line in image:
            if line[row] == "1":
                hasOne = True
                break
        return hasOne
    # py 简洁版
    def checkRow(image,row):
        return any(line[row] == "1" for line in image)
```
# solution 1
```py
# 找可行区间
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def checkRow(image,row):
            hasOne = False
            for line in image:
                if line[row] == "1":
                    hasOne = True
                    break
            return hasOne
            
        def checkLine(image,line):
            return "1" in image[line]
        
        def getWidth(image,x,y):
            n = len(image[0])
            # find min "1" in 0 - y 
            lo, hi = 0, y
            while lo < hi:
                mid = (lo+hi)//2                                 
                if checkRow(image,mid):
                    hi = mid
                else:
                    lo = mid + 1
            lower = lo
            
            # find max "1" in y - n
            lo,hi = y,n-1
            while lo < hi:
                mid = (lo+hi)//2
                if checkRow(image,mid):
                    if lo == mid:
                        if checkRow(image,hi): lo += 1
                        else: hi -= 1
                    else:
                        lo = mid
                else:
                    hi = mid - 1
            upper = hi
            return upper - lower + 1
        
        def getHeight(image,x,y):
            m = len(image)
            # find lower in [0,x]
            lo,hi = 0,x
            while lo < hi:
                mid = (lo+hi)//2
                if checkLine(image,mid):
                    hi = mid
                else:
                    lo = mid + 1
            lower = lo
            
            # find upper in [x,m-1]
            lo,hi = x,m-1
            while lo < hi:
                mid = (lo+hi)//2
                if checkLine(image,mid):
                    if lo == mid:
                        if checkLine(image,hi): lo += 1
                        else: hi -= 1
                    else:
                        lo = mid
                else:
                    hi = mid - 1
            upper = lo
            return upper - lower + 1
        
        return getWidth(image,x,y) * getHeight(image,x,y)
```