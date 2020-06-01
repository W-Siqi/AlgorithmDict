# take away
这是design题目里面比较常见的一类： 设计数据结构保持存取复杂度尽可能小。（**一般用hash就可以把存取降到O(1)**）  
但这题难的是，因为多个关联信息（时间和已出现频率），所以要用不止一个hash。 感觉有点像设计数据库。  

# 踩坑
## 常见错误：
忘记的维护latest之类的变量，比如timestamp,freq，numbers之类的东西，都是要保证都是最新的，一旦有变动都要跟着改！
## list.remove() & tuple
python的tuple可以当做常量来remove(不知道element是[]的时候，或者引用的时候，remove会怎么处理)
## 算法一定要考虑最坏的情况！
比如，都只出现freq都是1，hash获取得到的是常常的数组。这个时候如果不做优化，就是O(N)而不是O(1)!

# 简洁代码
- pop本身有返回值的，所以不用先存了再pop  
- 使用defaultdict  
- if not li: 走的是False,如果li == []，即空list
# solution1
基本思路是numbers{} hash出现的次数  
freq{} hash对应出现次数的number  
number_timestamps hash出现的时间记录    
为了保证pop的更新效率，freq的value[]的number，是按照时间戳排放(类似优先级队列)
```py
class FreqStack(object):

    def __init__(self):
        self.timestamp = 0
        self.number_timestamps = {}
        # key: numbers values ccured times
        self.numbers = collections.Counter()
        # key: frequence values:[(number,timestamp),...]
        self.freq = {}
        self.max_freq = 0
        
    def push(self, x):
        self.timestamp += 1
        # update numbers
        self.numbers[x] += 1
        # update freq
        if self.numbers[x] not in self.freq:self.freq[self.numbers[x]] = []
        self.freq[self.numbers[x]].append((x,self.timestamp))
        # 一个小优化，定向remove可比遍历强多了。但是如果能二分，或者hash可能会更好！
        if self.numbers[x] - 1 > 0:
            self.freq[self.numbers[x]-1].remove((x,self.number_timestamps[x][-1]))
            
        # update timestamp
        if x not in self.number_timestamps:
            self.number_timestamps[x] = []
        self.number_timestamps[x].append(self.timestamp)
        
        self.max_freq = max(self.max_freq,self.numbers[x])

    def pop(self):
        if self.max_freq == 0: return 0
        
        # pick and pop
        resnum =  self.freq[self.max_freq][-1][0]
        self.freq[self.max_freq].pop()
        if len(self.freq[self.max_freq]) == 0: 
            del self.freq[self.max_freq]
            
        # update numbers
        self.numbers[resnum] -= 1
       
        # update timestamps
        self.number_timestamps[resnum].pop()
        if self.numbers[resnum] > 0: 
            new_timestamp = self.number_timestamps[resnum][-1]
            # update new freq 
            new_freq = self.numbers[resnum]
            freq_list = self.freq[new_freq]          
            lo,hi = 0,len(freq_list)
            while lo < hi:
                mid = (lo+hi)//2
                if freq_list[mid][1] < new_timestamp:
                    lo = mid + 1
                else:
                    hi = mid
            freq_list.insert(lo,(resnum,new_timestamp))
            
        while self.max_freq > 0 and self.max_freq not in self.freq:
            self.max_freq -= 1
                           
        return resnum
```

# solution 2(1的改进版)
我当时为了“方便插入”，freq[]里是(number,timestamp)这种tuple.  
因为我看number的时候，需要知道对应的timestamp.  
BUT！ **需要只要对应的timestamp(或其他信息),可以通过单独创建一个hashmap来查询**，何况这里本身就有number_timestamps！ 
```py
class FreqStack(object):
        ....
        # 改动1
        if self.numbers[x] not in self.freq:self.freq[self.numbers[x]] = []
        self.freq[self.numbers[x]].append(x)
        
        if self.numbers[x] - 1 > 0:
            self.freq[self.numbers[x]-1].remove(x)
            
        ...
        new_freq = self.numbers[resnum]
        freq_list = self.freq[new_freq]          
        lo,hi = 0,len(freq_list)
        while lo < hi:
            mid = (lo+hi)//2
            # 改动2
            if  self.number_timestamps[freq_list[mid]][-1] < new_timestamp:
                lo = mid + 1
            else:
                hi = mid
        freq_list.insert(lo,resnum)
            
        ...
```

# solution 3(超级妙！)
## 根本不需要维护一个timestamp
这里直接用stack的插入顺序当timesample。  
## 如果回溯timesamp？
比如次数从4增加到5的时候，freq[4]里面不要删掉那个就行了。  
**细细品味，其实有时候不一定要这么清白，freq[times]不一定要存当前的...**
```py
class FreqStack(object):

    def __init__(self):
        self.numbers = collections.Counter()
        self.freq = collections.defaultdict(list)
        self.max_freq = 0
        
    def push(self, x):
        self.numbers[x] += 1
        self.freq[self.numbers[x]].append(x)           
        self.max_freq = max(self.max_freq,self.numbers[x])
        

    def pop(self):
        if self.max_freq == 0: return 0
        
        resnum = self.freq[self.max_freq].pop()
        self.numbers[resnum] -= 1
        # 其实这个while改成if都可，因为num出现了5次，那么取出去一个，至少frequency 4还是在的。
        while self.max_freq > 0 and not self.freq[self.max_freq]:
            self.max_freq -= 1
                           
        return resnum
```

# solution4 (priority queue)
这里巧妙的地方，和solution3一样，在于不用那么严格的保证一个number只存一次。  
比如有5个num，那么这个priority_queue就有5个item是对于num的，分别对于它第1,2,3,4,5次出现的时候。  
出现5次的先pop，然后4,3,2,1...  
## 延伸：双优先级的priority_queue
我觉得这个解法的intuition就是，在原来stack按照时间顺序的情况下，保证次数多的排在前面。   
其实就是，次数最优先，出现时间次优先的排序。  
这种情况下就可以用这个类似的解法...

```py
class FreqStack:

    def __init__(self):
        self.heap = []
        self.m = collections.defaultdict(int)
        self.counter = 0
        
    def push(self, x):
        self.m[x]+=1
        heapq.heappush(self.heap,(-self.m[x], -self.counter, x))
        self.counter+=1
    
    def pop(self):
        toBeRemoved = heapq.heappop(self.heap)
        self.m[toBeRemoved[2]]-=1
        return toBeRemoved[2]
```