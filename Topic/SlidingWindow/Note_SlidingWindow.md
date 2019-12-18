# When use sliding window
When need to treversal the **subarray**,  

sliding window is a technique to reduce complexity from  O(n^2)  to  O(n)

# Natrual of Sliding Window    
#### skip impossible cases, only traveral the unknown situations.  
when finish a round of subarray checking, we can based on previous infomation to:  
 **skip many checking**(because it is definitely impossible)  
 or **reuse the result** on the next round.   
   
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

### when stop?  
end pointer meet a character that of in the hash.(this character can not fit into the permuation)  

### how we start next round?
move the start pointer, when a[start] == a[end -1]. because we fail because end ponter add character that is not fit, so we remove charater from start pointer till we find this character that is not fit.

## 2- Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/ 

### trick here:
same to the "permuation in string": use hash[124] to record current remainng count for specific character.
### when stop 
after end pointer meet the element, subarray has contained all the chacracters  

### how we start the next round?   
1- move start pointer, till after move the character the subarray cannot satisfy the requirement.  
2- record the result  
3- reamin the start pointer  
(PS： cannnot move start to end, becasue we cannot sure if the optimal solution may...)

## 3- Max Consecutive Ones III 
https://leetcode.com/problems/max-consecutive-ones-iii/

### trick here:  
always find the earliest index: use queue to record the histroy

### whene stop 
meet 0 and used up all the chances

### how we start the next round?
the next index of the earliest index when we turn 0 to 1,  
because any index before this, will also stuck in the same position where current end pointer is.  
but any index after is ensure.   
This indicates the basic stratigy of sliding window: skip the impossible cases, only traveral the unknowns.

## 4- Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/
### how to define satrt & end  
one way is, 'start' always means the first elemnt in the array, 'end' means the next element to extend...  
initally, start = 0, end = 1.  

### frequenly mistake  
forget the check the case at the edge, which is the case when escape the while{} loop.

### count qualified cases VS optimal case
when to restart to the next turn, I firstly unconciously move the start ponter till...  
however this is to count the qualified cases, I made mistakes in skipping impossible cases...