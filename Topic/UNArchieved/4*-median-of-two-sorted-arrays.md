solution1:
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # decide the position of median number(s)
        pos1 = pos2 = 0
        m,n = len(nums1),len(nums2)
        if (m+n)%2 == 0:
            pos1 = (m+n)/2
            pos2 = pos1 + 1
        else:
            pos1 = pos2 = (m+n)//2 + 1

        # find the median numbers
        counted = p1 = p2= mid1 = mid2 = 0
        while counted < max(pos1,pos2):
            val = 0
            if p1 >= m:
                val = nums2[p2]
                p2 += 1
            elif p2 >= n:
                val = nums1[p1]
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                val = nums1[p1]
                p1 += 1
            else:
                val = nums2[p2]
                p2 += 1
                
            counted += 1
            if counted == pos1:
                mid1 = val
            if counted == pos2:
                mid2 = val
                
        return (mid1+mid2)/2
```