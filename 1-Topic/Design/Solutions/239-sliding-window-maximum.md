# 跟踪queue的最大值
暴力的是O（N）  
额外创建heap，priorityqueue之类的，做到O（lgN）  
## 但是由于这题queue增加删除的有序性，可以做到接近O（1）！！
核心还是一个priorityqueue，但是删除和增加，都是可以删queue里面的元素。  
因为添加一个值a，那么就可以吧queue里面所有比这个小都pop掉(因为比a老又比a小，是永无天日的)。  
pop一个值的时候...
# solution
```py
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        window = collections.deque()
        res = []
            
        for end in range(len(nums)):
            if end >= k:
                while window and window[-1] == end-k:
                    window.pop()
          
            while window and nums[window[0]] < nums[end]:
                    window.popleft()
            window.appendleft(end)
                
            if end >= k-1:
                res.append(nums[window[-1]])
        return res
```