```py
class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def canRemoveOne(occur):
            if len(occur) > 2:
                return False
            
            if len(occur) == 1:
                k = occur.keys()[0]
                if k == 1 or occur[k] == 1: return True
                else: return False
            
            if len(occur) == 2:
                k1,k2 = min(occur.keys()[0],occur.keys()[1]),max(occur.keys()[0],occur.keys()[1])
                v1,v2 = occur[k1],occur[k2]
                if v1 > 1 and v2 > 1:  return False
                if v1 == 1 and k1 == 1: return True 
                if v2 == 1 and k2 - 1 == k1:  return True
        
            return False
        
        record = {}
        occur = {}
        res = 0
        for i,n in enumerate(nums):
            if n in record:
                record[n] += 1
                # add record[n]
                if record[n] in occur: occur[record[n]] += 1
                else: occur[record[n]] = 1
                # remove record[n]-1
                occur[record[n]-1] -= 1
                if occur[record[n]-1] == 0:  del occur[record[n]-1]
            else:
                record[n] = 1
                # add record[1]
                if 1 not in occur:  occur[1] = 1
                else:  occur[1] += 1
            # print(canRemoveOne(occur),occur)
            if canRemoveOne(occur):
                res = max(res,i+1)
        
        return res
```