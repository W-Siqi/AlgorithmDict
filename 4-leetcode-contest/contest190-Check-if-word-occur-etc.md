# string 的常用函数
这题思路简单，核心就是怎么用python把他给写简洁了。     

当时的不简洁写法：
```py
# 主要是手撸了split和startswith
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        counter = 0
        index = 1
        while counter < len(sentence):
            # match
            match = True
            for i in range(len(searchWord)):
                if searchWord[i] == sentence[counter]:
                    counter+=1
                else:
                    match = False
                    break
                    
            if match:
                return index
            else:
                while counter < len(sentence) and  sentence[counter] != ' ':
                    counter += 1
                counter += 1
                index += 1
                
        return -1
```

## tip1: py的split()
代码一下子短了很多
```py
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        for i,w in enumerate(sentence.split(' ')):
            if len(w) >= len(searchWord):
                isPrefix = True
                for j in range(len(searchWord)):
                    if searchWord[j] != w[j]:
                        isPrefix = False
                        break
                if isPrefix:
                    return i + 1
        return -1
```
如果再不要脸一点，用py的startswith
```py
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        for i,w in enumerate(sentence.split(' ')):
            if w.startswith(searchWord):
                return i + 1
        return -1
```
## tip2：find
这方法巧是巧，但这题不是那么使用。  
但是find()这个方法还是要记一下的~  

核心代码：
```py
(' ' + sentence).find(' ' + searchWord); 
```