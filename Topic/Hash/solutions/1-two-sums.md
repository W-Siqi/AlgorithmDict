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