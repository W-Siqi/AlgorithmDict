class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        curSum = nums[0]
        start, end = 0,1
        res = 1 if curSum >= s else 0
        while start < len(nums):
            # expend 'end' as far as we can
            while curSum < s and end < len(nums):
                curSum += nums[end]
                end+=1
                
            # record res
            if(curSum >= s):
                if(res == 0):
                    res = end - start
                else:
                    res = min(res,end - start)
            
            # preprare for the next round
            curSum -= nums[start]
            start += 1
            
        return res
        
        
        