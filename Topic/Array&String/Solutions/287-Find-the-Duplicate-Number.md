# solution 1 - just rank
```py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]    
```

# solution 2 - 用in-place hash(和442 一样)
```py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num)] < 0: return abs(num)
            else: nums[abs(num)] *= -1
```
# solution 2 - 天时地利人和的巧解
因为 1 < a[i] <len(a), 所以我们可以吧a[i]的值当做一个指针。  
因为又且只有一个重复，而且数字比范围正好多1， 所以这个指针状况是一个带环的链表
```py
def findDuplicate(self, nums):
    slow = fast = finder = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            while finder != slow:
                finder = nums[finder]
                slow = nums[slow]
            return finder
```