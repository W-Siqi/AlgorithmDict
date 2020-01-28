dont use , because the case like(99999999/1)
```python
    while dividend >= divisor:
        dividend -= divisor
        sum += 1
```

deside the factor
```python
factor = 1 if dividend*divisor  >0 else -1
```

edge case -int_max  will ...becasue [-pow(2,31),pow(2,31)]
better solution when 10000000/1
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor ==0:
            return 0
        
        factor = 1 if dividend*divisor  >0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        while dividend >= divisor:
            num = 1
            while divisor * num <= dividend:
                num *= 10
            
            dividend -= divisor*(num/10)
            res += (num/10)
        
        res = int(res*factor)
        res = min(res,pow(2,31)-1)
        return res
```