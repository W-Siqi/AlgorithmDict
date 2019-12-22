class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        dct = {}      
        # init the pos of two pointers
        p1,p2= 0,1
        res = 1
        dct[s[p1]] = 1
        
        while p2 < len(s):
            # adjust p1
            if s[p2] not in dct:
                pass
            else:
                res = max(res,p2-p1)
                while p1 < p2 and s[p2] in dct:
                    del dct[s[p1]]
                    p1+=1
            # add s[p2] to queue
            dct[s[p2]] = 1
            p2 += 1
        else:
            res = max(res,p2-p1)
            
        return res
        
        