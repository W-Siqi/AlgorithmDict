# edge case: 'aa' 对 'ab' ，所以在存映射的时候，a->b， 意味着：之后所有的映射，a->x 和 x->b都不行。 
```py
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = {}
        mapped = set()
        for i in range(len(s)):
            if t[i] not in mapping:
                if s[i] not in mapped:
                    mapping[t[i]] = s[i]
                    mapped.add(s[i])
                else:
                    return False
                
            elif mapping[t[i]] != s[i]:
                return False
        return True
```