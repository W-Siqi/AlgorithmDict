# Solution 1
force the sequece to ensure the unique combination
```py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        def dfs(path,cur_sum,candidates,cur_pos,target):
            if cur_pos >= len(candidates):
                return []
            
            res = []
            while cur_sum <= target:
                # call child or add result
                if cur_sum == target:
                    res.append(path.copy())
                    break
                else:
                    res += dfs(path.copy(),cur_sum,candidates,cur_pos+1,target)
            
                # add one more number
                path.append(candidates[cur_pos])
                cur_sum += candidates[cur_pos]
                
            return res
        
        
        return dfs([],0,candidates,0,target)
```