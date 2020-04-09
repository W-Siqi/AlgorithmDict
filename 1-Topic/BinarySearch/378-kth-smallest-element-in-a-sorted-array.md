# key&tag
heap, binary search

# solution1
这个solution告诉了我一个道理，logN是极其小，极其接近O(1)的。  
这里即使log2(max-min)也超级快，记住log2(2199999999)也才32左右！  
(另外，这题真的是，见过最复杂的二分了...)
```py
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def lowerBound(arr,target):
            lo,hi = 0, len(arr)
            while lo < hi:
                mid = (lo+hi)//2
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
       
        # return count,smaller geater
        def countSmaller(matrix,num):
            count, smaller, greater = 0, -float("inf"), float("inf")
            for i in range(len(matrix)):
                if matrix[i][0] <= num:
                    lbound = lowerBound(matrix[i],num)
                    count += lbound
                    if lbound < len(matrix[i]):
                        greater = min(greater,matrix[i][lbound])
                    if lbound - 1 >= 0:
                        smaller = max(smaller,matrix[i][lbound-1])
                else: # 这里不能漏！有edge case！ 万一开头就是greater怎么办？
                    greater = min(greater,matrix[i][0])
                    break
            return count, smaller, greater
        
        targetSmaller = k-1
        lo,hi = matrix[0][0],matrix[-1][-1]
        while lo < hi:
            mid = (lo+hi)//2
            count,smallerNum,greaterNum = countSmaller(matrix,mid)
            if count < targetSmaller:
                lo = mid + 1
            else:
                hi = mid
        # 此时，lo 恰好有k-1个数比它小，或者 n(n>=k)个比他小
        # 前者，直接找matrix 最接近lo的数bigger数
        # 后者，找最接近lo 的smaller数
        count,smallerNum,greaterNum = countSmaller(matrix,lo)
        if count > targetSmaller:
            return smallerNum
        else: # count == targetSmaller
            return greaterNum
```
