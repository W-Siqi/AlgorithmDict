# solution 1 - pure hash
```py
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        record = [False]*(len(nums)+1)
        res = []
        for num in nums:
            if record[num]:
                res.append(num)
            else:
                record[num] = True
        return res
```

# solution 2 - in-place hash
使用正负号做标记，这样abs一下就不妨碍原数据
```py
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return res
```