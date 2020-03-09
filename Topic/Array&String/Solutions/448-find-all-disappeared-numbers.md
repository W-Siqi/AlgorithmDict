# solution 1
```py
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = [0] * (len(nums) + 1)
        for num in nums:
            count[num] += 1
        
        res = []
        for i in range(1,len(nums)+1):
            if count[i] == 0:
                res.append(i)
        
        return res
```