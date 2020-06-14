# 优雅解法- Binary Search
类似的策略我是见到过的，但是当时没反应出来。  
## “大数定理”->二分尝试
大数定理说的是，样本越大越好。  
这类情形一样，天数是越多越好。  
在这种正向趋势前面找临界点（最优值），都可去二分的去尝试。  
比如n天行不通，那尝试的方向就是n往上，反之往下，这样就做到了二分。

参见： 
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/686316/JavaC%2B%2BPython-Binary-Search
# 头铁解法 - 区间merge + Binary search
另一个思路就是，每次你加1朵花，你能快速判断当前的情形吗？  
可以！可以做到O（lgN）    

Intuiaon：
- 这里区间不可能重叠，这样就可以进行排序，O（lgN）找到相关区间
- 找到相关区间后，花团的数量这需要更新这1个相关区间的值就行了O（1） （类似于脏数据更新）

```py
class Solution(object):
    def minDays(self, bloomDay, m, k):
        dayflo = collections.defaultdict(list)
        for i,day in enumerate(bloomDay):
            dayflo[day].append(i)
        
        daylines = sorted(dayflo.keys())
        bnums = 0
        b = []
        for d in daylines:
            for flo in dayflo[d]:
                # add flower 二分找插入位置
                lo ,hi = 0,len(b)
                while lo < hi:
                    mid = (lo+hi)//2
                    if b[mid][0] < flo:
                        lo = mid + 1
                    else:
                        hi = mid
                
                merged = False

                # 4种merge情况讨论，并更新情况
                if lo < len(b) and b[lo][0] == flo + 1:
                    merged = True
                    bnums -= (b[lo][1]-b[lo][0]+1)//k
                    b[lo][0] = flo
                    bnums += (b[lo][1]-b[lo][0]+1)//k

                if lo-1 >= 0 and b[lo-1][1] + 1 == flo:
                    merged = True
                    bnums -= (b[lo-1][1]-b[lo-1][0]+1)//k
                    b[lo-1][1] = flo
                    bnums += (b[lo-1][1]-b[lo-1][0]+1)//k
                    
                if lo < len(b) and lo-1>=0 and b[lo-1][1] == b[lo][0]:
                    bnums -= (b[lo][1]-b[lo][0]+1)//k
                    bnums -= (b[lo-1][1]-b[lo-1][0]+1)//k
                    b[lo-1][1] = b[lo][1]
                    bnums += (b[lo-1][1]-b[lo-1][0]+1)//k
                    b.pop(lo)
                    
                if not merged:
                    b.insert(lo,[flo,flo])
                    bnums += 1//k
                #print("add",flo,b)
            if bnums >= m:
                return d
        return -1
```