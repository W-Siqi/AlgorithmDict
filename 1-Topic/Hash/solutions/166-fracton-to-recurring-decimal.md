# edge case: 
1. 考虑负数
2. 分子大于分母
3. 整好整除，没小数部分

# solution 
出现循环小数的条件，其实就是，被除数第二出现了！
```py
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return 0
        isNeg = numerator*denominator < 0
        numerator,denominator = abs(numerator),abs(denominator)
        
        res = str(numerator//denominator)
        remain = (numerator%denominator)*10
        if remain == 0:
            return res if not isNeg else "-"+res
        else:
            res += '.'
            
        visited = {}
        pos = len(res)
        while remain != 0:
            if remain not in visited:
                visited[remain] = pos
                pos += 1
                res+=(chr(ord('0')+remain//denominator))
                remain = (remain%denominator)*10
            else:
                repeat = "("+ res[visited[remain]:]+")"
                res = res[:visited[remain]]+repeat
                break
        return res if not isNeg else "-"+res
```              
            