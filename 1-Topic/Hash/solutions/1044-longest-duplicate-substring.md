# TLE solution O(lgN) ~ O(n*n) 
这题的思路是，比如从字母a开始搜，那么只要定向找a开始的就行了，这就想到了hash进行a-z的归组这样一轮轮下来再就ok了。  
- 最好的情况，就是abcd...z比较匀称分布，O(log26N)  
- 最差的情况，就是全是单一字母，归类了等于没归O(N*N)
```py
class Solution(object):
    def longestDupSubstring(self, S):
        def match(preStr,candi):
            alp = {}
            for index in candi:
                if index >= len(S):
                    continue
                    
                if S[index] not in alp:
                    alp[S[index]] = [index+1]
                else:
                    alp[S[index]].append(index+1)
            
            res = preStr
            for k,v in alp.items():
                if len(v) > 1:
                    post = match(preStr+k,v)
                    if len(post) > len(res):
                        res = post

            return res
        
        # key: 'a'... value: [index1,index2](index is the next letter) 
        candi = [x for x in range(len(S))]
            
        return match("",candi)
```
# AC solution binary search
这里的灵感就是：**如果是找定长的substring，那么是很方便的，用hash做做到O(N)**  
## 这里hash的作用： 匹配查重

## 字符串的hash函数
这里遍历每个子字符串需要计算hash值，虽然可以直接把字符串当做key，但是这个构建key的过程是O(k)的。  
- 所这里吧字符串看做26进制的数字
把他转成10进制的就行了，**但是注意要取mod！**，不然字符串超长不论是时间还是空间都吃不消

## 代码优化：见注释
```py
class Solution(object):
    def longestDupSubstring(self, S):
        # 优化1： 缓存S对于的ASCII值，因为
        # 1）这里频繁访问，可以省下速度
        # 2） 简化代码，不然每次出现都要写ord()...在嵌套数学式里面很繁琐
        A = [ord(c)-ord('a') for c in S]
        def test(l):
            if l <= 0: return ""
            seen = set()
            value,mod = 0,2**63-1
            # 优化2： 缓存每次取掉头部的pow！ 要意识到在l很长的时候，这是一个O(k)的操作！
            font_base = pow(26,l,mod)
            for i in range(len(S)):
                # update hash value
                if i >= l: value = (value - A[i-l]*font_base)%mod
                value = (26*value+A[i]*26)%mod
                
                # check record 
                if i >= l - 1:
                    if value in seen:return S[i-l+1:i+1]
                    else: seen.add(value)
                                 
            return ""
        
        lo,hi = 0,len(S)
        while lo < hi:
            mid  = (lo+hi)//2
            if test(mid) != "":
                lo = mid + 1
            else:
                hi = mid
        return test(lo-1)
```

# solution3： surfix array
这个先挖个坑，这trie tree一样，不太像是能在当场写完的算法