# debug- 脑子重写跑一边用例，是很好的方法。因为很多bug，是因为写的时候，脑子的流程跑错了，误以为会这么走。而且一些笔误也容易发现。

# solution1: move元素的一个小技巧
还是这个最好理解，最简洁
```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] == 0: zeroCount += 1
            else: nums[i-zeroCount] = nums[i]
        for i in range(1,zeroCount+1):
            nums[-i] = 0
```

# solution2（误区）： 快排的partition算法？
这题不可以！因为快排只能保证右边全是0，但是顺序会被打乱！

# solution3: 伪冒泡
一次遍历，如发现不是0的，就往前冒泡，遇到0就往前冒。  
作为优化的话，可以用lastfoundzero 来记录当前最前面的。这样避免了1,2,3,4,0,0,0,0,5的时候，5要冒泡4次才到前面。 