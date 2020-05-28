# motivation
这里查黑名单，最快的就是hash，很自然。

# hash的冲突
这里的关键是，要考量黑名单特别长的情况。
这种情况下，无论是random到中了为止，还是往后顺延到合理地数，都无法做到O(1)。  
这很像hash，在冲突极端的情况下，查询的O(n)

# solution 1
在黑名单的长度比率超过阈值的时候，创建白名单。  
直接在白名单里面随机。

# solution 2
重映射。这里不是简单的重映射，这里只映射了白名单index范围内的在黑名单的数。

是这位老哥的解法：
https://leetcode.com/problems/random-pick-with-blacklist/discuss/144624/Java-O(B)-O(1)-HashMap  
核心思路是, 白名单的长度我是知道的，设为M。  
对于0~M的index， index本身的数：
- 如果不在黑名单，那么对应的数就是index本身  
- 如果再黑名单，那么就映射到其他白名单。