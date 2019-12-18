class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree:
            return 0
        
        # record the earlest index of the type
        curTypes = {}
        start, end = 0, 0
        res = 0
        
        while start < len(tree):
            # picke as much as it can
            while end < len(tree):
                if tree[end] in curTypes or len(curTypes) < 2:
                    curTypes[tree[end]] = end
                    end += 1
                else:
                    break
            
            # record
            res = max(res,end - start)
            
            # preprare for nex round
            if end >= len(tree):
                # no need 
                break
                
            minIndex = len(tree) + 10
            for key in curTypes:
                if curTypes[key] < minIndex:
                    minIndex = curTypes[key]
            
            start = minIndex + 1
            curTypes.clear()
            curTypes[tree[end - 1]] = end - 1
        
        return res
            
                    