# two pointers, extention of ...

# start 和 end 的含义，到底包括不包括...
# 出去的edge case 要不要算的问题
# 退出的依据, start or end...

# EXAMPLES
## 0- 3 sum   
## 0- 3 sum close to target


## 003- Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/  

basically the same with sliding window.  
when fail, start based on the previous ...  

## 209- Minimum Size Subarray Sum  
https://leetcode.com/problems/minimum-size-subarray-sum/  
same tactic ... 
思考结束依据，是以start 还是end...

## 3- Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/  
这里是的小技巧，是分offset，每个offset进行sliding window...

题目看清！！！words里可能会是重复的！！  

musk{}, remain{} 这种状态维护的是高度危险区，因为每一处涉及修改的，都要维护。而刷题的时候，一般处于时间考虑不会吧这种耦合而操作封装在一起。只会进行’人工耦合‘

## 904. Fruit Into Baskets