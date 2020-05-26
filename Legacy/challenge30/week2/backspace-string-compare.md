 # solution1:
 ```py
 # 1- python 反向遍历数组： for n in nums[::-1]:
# 2- edge case: # 出现多余
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def getStr(src):
            stack  = []
            for s in src[::-1]:
                if s == '#':
                    stack.append(s)
                else:
                    if len(stack) > 0 and stack[-1] == '#':
                        stack.pop()
                    else:
                        stack.append(s)
            while len(stack) > 0 and stack[-1] == '#':
                stack.pop()
                
            res =  "".join(stack)
            print(res)
            return res
        
        return getStr(S) == getStr(T)
 ```

# solution2(编译不通过，仅仅思路)
```py
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def processStr(src):
            cur = len(src) - 1
            backSpaceRemain = 0
            while cur >= 0:
                if src[cur] != '#' and backSpaceRemain > 0:
                    backSpaceRemain -= 1
                    del src[cur]
                elif src[cur] == '#':
                    backSpaceRemain += 1
                cur -= 1
                
        
        processStr(S)
        processStr(T)
        return S ==T
```