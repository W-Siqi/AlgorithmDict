# main
这题主要是创造二分的动机，  
因为频繁查询， 但这里是index的位置都有关系的，不能随意排序。   
但是我们可以从后往前数，数过的就可以直接排序。
# 【填坑】
binary index tree
# solution 1
```py
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def lowerBound(arr,target):
            lo,hi = 0, len(arr)
            while lo < hi:
                mid = (lo+hi)//2
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        def upperBound(arr,target):
            lo,hi = 0, len(arr)
            while lo < hi:
                mid = (lo+hi)//2
                if arr[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        sortedBack = []
        res = 0
        for i in range(len(nums)-1,-1,-1):
            # find target num
            target = nums[i]//2 if nums[i]%2 == 1 else nums[i]//2 - 1
            lb = upperBound(sortedBack,target)
            res += lb
            # insert pos
            insertPos = lowerBound(sortedBack,nums[i])
            sortedBack.insert(insertPos,nums[i])
        
        return res
```