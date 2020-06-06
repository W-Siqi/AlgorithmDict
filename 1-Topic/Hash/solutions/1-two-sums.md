# motivation
hash最常见的动机：如果要在一堆元素里面频繁查找（通常遍历查询N次），那么就构建hash

if build the hash first:
dont forget to check use the one number twice
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i,num in enumerate(nums):
            m[num]=i
        for i,num in enumerate(nums):
            if target - num in m and i != m[target - num]:
                return i,m[target - num]
        
        return []
```