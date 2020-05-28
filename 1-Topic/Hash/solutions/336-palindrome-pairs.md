# takeway
## trie树
优化遍历式查找的手段，之前有两个。一个是二分，一个是hash。  
这里solution3出现了一个常见的情形: trie tree查找  
## 大海捞针VS有的放矢
solution 4就是用hash， 这里想到hash最大的一个障碍，就是意识到，要去吧这个遍历check问题，转化为定向查找问题。  
逐个遍历是大海捞针，找前缀是有的放矢，是个查找问题。意识到这可以转化为查找问题，那么就好办了，当然是hash她啊！

# solution 1(naive, O(n^2*k))
```py
  def palindromePairs(self, words):
        def isPalindorm(w):
            left,right = 0,len(w)-1
            while left <= right:
                if w[left] != w[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True

        res = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPalindorm(words[i]+words[j]):
                    res.append([i,j])
                if isPalindorm(words[j]+words[i]):
                    res.append([j,i])
        return res           
```

# solution2(反向优化的案例)
常见的优化思路就是，先用小成本粗判定来当过滤器，通过测试了再进行最后的细判。  
构成回文的一个条件，就是a-z出现次数最多一次为奇数，这个solution就是按照这个思路来粗判。  
但是**通过的testcase反而少了，是负优化** ：  
因为粗判的代价还是太大，而且回文判定的效率本身就是O(N),是比较高了，这个粗判O(26)可能比直接判回文都要慢！
## 教训： 优化的时候，考虑O()做数量级的优化，然后再考虑剪枝，同数量级的优化意义不一定大
同数量级的优化，不但意义不大。而且没有测试，很可能出现负优化。
```py
  def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindorm(w):
            left,right = 0,len(w)-1
            while left <= right:
                if w[left] != w[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True
        
        def possible(info1,info2):
            flag = False
            for i in range(26):
                if (info1[i]+info2[i])%2 == 1:
                    if flag: return False
                    else: flag = True       
            return True
        
        infos = []        
        # calcutae info a-z
        for w in words:
            info = [0]*26
            for c in w:
                info[ord(c)-ord('a')] = (info[ord(c)-ord('a')] + 1)%2
            infos.append(info)
        
        res = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not possible(infos[i],infos[j]):
                    continue
                if isPalindorm(words[i]+words[j]):
                    res.append([i,j])
                if isPalindorm(words[j]+words[i]):
                    res.append([j,i])
        return res
            
```

# solution 3(trie tree)
这个拼起来是回文，其实就是转化为找前缀。  
找前缀这个东西，就可以用trie tree来优化，吧O(N)优化到O(k)

# solution 4(hash)
找前缀这个点，除了trie树之外，可以直接一个个猜前缀，然后用hash找。  
这个方法也是O(n* k* k), 而且实现起来，比trie树要简单（说实话，trie不像是刷题的算法...）
  

  
这个算法曾在我的脑子里一闪而过，当时遇到的难题是，wordi遇到比它长的wordj了怎么办？难道wordj要存很多地方来确保wordi能找到？  


## edge cases
空字符串""  
自己和自己回文

```py
class Solution(object):
    def palindromePairs(self, words):

        def isPalindorm(w):
            return w == w[::-1]
        
        wo_dict = {word:i for i,word in enumerate(words)}
        res = []
        for word in words:
            if word == "":
                for another_word in words:
                    if isPalindorm(another_word) and another_word != word:
                        res.append([wo_dict[word],wo_dict[another_word]])
            for i in range(len(word)):
                pre = word[:i]
                back = word[i:]
                if isPalindorm(back):
                    reversePre = pre[::-1]
                    if reversePre in wo_dict and reversePre != word:
                        res.append([wo_dict[word],wo_dict[reversePre]])
                if isPalindorm(pre):
                    reverseBack = back[::-1]
                    if reverseBack in wo_dict and reverseBack != word:
                        res.append([wo_dict[reverseBack],wo_dict[word]])
                        
        return res
            
```