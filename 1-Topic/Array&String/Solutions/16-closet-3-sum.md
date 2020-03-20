```py
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 
        
        first = 0
        minDiff = float("inf")
        res = 0
        nums.sort()
        while first < len(nums) - 2:
            second = first + 1
            third = len(nums) - 1
            while(second < third):
                s = nums[first] + nums[second] + nums[third]
                if abs(s - target) < minDiff:
                    minDiff = abs(s - target)
                    res = s
                if s == target:
                    return s
                elif s > target:
                    third -= 1
                else:
                    second += 1
            first += 1
        
        return res
```