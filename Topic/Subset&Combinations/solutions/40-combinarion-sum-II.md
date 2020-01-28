# solution1
```py
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates,path,path_sum):
            if not candidates:
                return []
            
            res = []            
            cand = candidates[0]
            cand_num = 0
            while cand_num < len(candidates) and candidates[cand_num] == cand: cand_num += 1
            
            for i in range(0,cand_num+1):
                new_sum  = path_sum + cand*i
                if new_sum == target:
                    res.append(path+[cand]*i)
                elif new_sum < target:
                    res += dfs(candidates[cand_num:],path+[cand]*i,new_sum)
            
            return res
        
        candidates.sort()
        return dfs(candidates,[],0)
```