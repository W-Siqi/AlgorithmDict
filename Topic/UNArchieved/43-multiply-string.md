 
 solution1: 
 ```py
 class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0]*(len(num1)+len(num2))
        
        for i,n1 in enumerate(num1):
            for j,n2 in enumerate(num2):
                mul = int(n1)*int(n2)
                div, mod = divmod(mul,10)
                res[len(num1)-i+len(num2)-j-2]+=mod
                res[len(num1)-i+len(num2)-j-1]+=div
        
        for i in range(len(res)):
            while res[i] > 9:
                res[i] -= 10
                res[i+1]+= 1
        
        while len(res)>0 and res[-1] == 0:
            res.pop()
        res.reverse()
        
        if res:
            return ''.join(map(str, res))
        else:
            return "0"
        
 ```