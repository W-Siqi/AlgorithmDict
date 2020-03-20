# solution 1
```py
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort()
        res = 0
        for fir in range(len(nums)-2):
            if nums[fir] == 0:
                continue 
            sec = fir + 1    
            thi = fir + 2
            while sec < len(nums) - 1:
                while thi < len(nums) and nums[fir] + nums[sec] > nums[thi]:
                    thi += 1

                res += max((thi - sec - 1),0)
                
                sec += 1
                thi = max(sec + 1, thi)
        return res
```

# solution2
```py
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort()
        res = 0
       
        for third in range(len(nums)-1,1,-1):
            first, second = 0, third - 1
            while first < second:
                # move first till meet requirement
                while first < second and nums[first] + nums[second] <= nums[third]:
                    first += 1
                
                # count 
                res += (second - first)
                
                # move first ahead
                second -= 1
                
        return res
```