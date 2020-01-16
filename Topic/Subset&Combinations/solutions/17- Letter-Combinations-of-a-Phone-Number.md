```python
# where to add the result...
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        letters = []
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for d in digits:
            letters.append(mapping[d])
            
        res = []     
        self.dfs(letters,0,"",res)
        return res
        
    def dfs(self, letters, nextl, path, res):
        if nextl >= len(letters):
            return 
        
        # traverse childs
        for l in letters[nextl]:
            npath = path + l
            
            # if reach the end...
            if nextl == len(letters) - 1:
                res.append(npath)
            else:
                self.dfs(letters,nextl+1,npath,res)
```