# solution 1 Hash
```py
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = collections.Counter(nums)
        for num,times in cnt.items():
            if times > n/2:
                return num
        return 0
```
# solution 2 Vote
```py
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = 0
        res = 0
        for num in nums:
            if vote == 0:
                res = num
                vote += 1
            elif num == res:
                vote += 1
            else:
                vote -= 1
        return res
```