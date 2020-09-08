# initical solution
## 不足1：
1. “每次调用最大的” -> 明显的heap/priority queue，这里没有必要自己造轮子
2.  实际上没有必要模拟，一共两种情况  
1) task充分利用，空隙正好被其他task填满了    
2） 有task个数太多，中间的空隙没task可填   
第一种，结果可以直接得出；而第二种，也是可以直接得出的！（冷却*次数+1），就是要注意一下最高个数的task可能存在并列的情况
```py
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskCountDict = collections.Counter(tasks)
        # [task,count]
        taskCountList = []
        for task,count in taskCountDict.items():
            taskCountList.append([task,count])
        taskCountList.sort(key = lambda x:-x[1])
        # [task,time]
        lastSTime = {}
        time = 1
        while len(taskCountList) > 0:
            # print ("time",time,taskCountList)
            for i in range(len(taskCountList)):
                task = taskCountList[i][0]
                if task not in lastSTime or time - lastSTime[task] > n:
                    # schedule it
                    # print("schedule",task)
                    lastSTime[task] = time                    
                    # update count info
                    taskCountList[i][1] -= 1
                    newCount = taskCountList[i]
                    if newCount[1] <= 0:
                        taskCountList.pop(i)
                    elif i + 1 < len(taskCountList) and newCount[1] < taskCountList[i+1][1]:
                        taskCountList.pop(i)                 
                        pos = 0
                        while pos < len(taskCountList) and taskCountList[pos][1] > newCount[1]: pos+=1
                        taskCountList.insert(pos,newCount)                                        
                    break
            time += 1
        return time - 1 
```