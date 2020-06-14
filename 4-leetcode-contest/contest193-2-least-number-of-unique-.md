#  frequency 优先的队列
和这题有点像：  
- [895-maxium-frequency-stack](./895-maxium-frequency-stack.md)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)  

可以创建priority queue， 不过这题不是要你具体枚举XXX，创建priority queue有点大题小做了。
# solution 1 直白解法 O(N*lgN)
```py
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        counts = collections.Counter(arr)
        times =  collections.Counter(counts.values())         
        tkeys = sorted(times.keys())
        i = 0
        while k > 0:
            if times[tkeys[i]] <= 0:
                i+=1         
            k -= tkeys[i] 
            if k >= 0:
                times[tkeys[i]] -= 1

        return sum(times.values())
```
# solution 1优化 bucket排序 O（N）
这里的N*lgN是因为sort进行了排序。  
但其实没必要排序，我们只需要记录最大值max，从1遍历到max就行了。  
## 相当于遍历bucket，因为我们知道最大值不超过N，所以bucket的数字很少