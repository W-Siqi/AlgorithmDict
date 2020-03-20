```py
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        
        res = 0
        nums.sort()
        for first in range(0,len(nums) - 2):
            sec = first + 1
            thi = len(nums) - 1
            while sec < thi:
                # move thi till smaller sum 
                while sec < thi and nums[first] + nums[sec] + nums[thi] >= target:
                    thi -= 1
                
                res += (thi - sec)
                
                # move sec
                sec += 1
        
        return res
```