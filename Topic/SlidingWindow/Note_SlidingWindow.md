# When use sliding window
When need to treversal the subarray,
sliding window is a technique to reduce complexity from  O(n^2)  to  O(n)

# Natrual of Sliding Window    
when finish a round of subarray checking, we can based on previous infomation to:  
 skip many checking(because it is definitely impossible)     
 or to reuse the result on the next round.   
   
For this reason: this most important question for sliding window is ,how we start for the next round of subarray traversal? 

# Implementation
two pointers: 
end pointer stands for the index that is going to check.   
start pointer stands for the start of the end pointer of this round.

# EXAMPLES
## 1- Permutation in String
https://leetcode.com/problems/permutation-in-string/  

### trick here:  
hash[124] to record the number the character..  
hash stands for the remaining character need to be add to form a permutation.  

### when fail?  
end pointer meet a character that of in the hash.(this character can not fit into the permuation)  

### how we start next round?
move the start pointer, when a[start] == a[end -1]. because we fail because end ponter add character that is not fit, so we remove charater from start pointer till we find this character that is not fit.

## 2- Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/  

## 3- Max Consecutive Ones III 
https://leetcode.com/problems/max-consecutive-ones-iii/

## 4- Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/