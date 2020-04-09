# main
这题和reverse pair极其相似  
其实说到底，确实是同样的情形，不同的外壳。

# 【填坑】
另一个和reverse pair相似的地方，是他们都有binary index tree的解法
# solution
edge case: range sum 还是那个问题，sum本身不减去任何东西
```py
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def lowerBound(arr,target):
            lo,hi = 0, len(arr)
            while lo < hi:
                mid = (lo+hi)//2
                if arr[mid] < target: lo = mid + 1
                else: hi = mid
            return lo
        
        def upperBound(arr,target):
            lo,hi = 0, len(arr)
            while lo < hi:
                mid = (lo+hi)//2
                if arr[mid] <= target:  lo = mid + 1
                else: hi = mid
            return lo   
        
        sums，s = [],0
        for n in nums:
            s += n
            sums.append(s)
        
        res = 0
        preSums = []
        for i in range(len(sums)):
            if sums[i] <= upper and sums[i] >= lower:
                res += 1
            # find previous with BS
            small = sums[i] - upper
            big  = sums[i] - lower
            s = lowerBound(preSums,small)
            b = upperBound(preSums,big)
            res += (b-s)
            
            # insert as asending pos
            insertPos = lowerBound(preSums,sums[i])
            preSums.insert(insertPos,sums[i])
        
        return res
```