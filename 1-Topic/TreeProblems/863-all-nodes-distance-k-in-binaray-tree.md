# solution 1（1.5pass）
核心思路：如果遍历的时候，遇到了targat,那么top-down的时候，更新depth。同时bottom-up返回时，也更新depth，同时对另一个child top-down更新depth。  
## 这类复杂情况问题：记得把case1,2,3,4...捋顺了再写
这题遍历到1个节点的时候，有以下几种case:
1. 我在target的子树下面
2. 我就是target
3. 我是target的parent
4. 我是target的同祖先的节点，但不是他的parent也不是他的child  
保证这4个case都不落下，就AC了
```py
class Solution(object):
    def distanceK(self, root, target, K):
        self.res = []
        def search(node,target,pre_distance):
            if not node: return -1
            
            self_distance = pre_distance
            # target as root
            if pre_distance >= 0:
                self_distance += 1
             
            # self as target
            if node == target:
                self_distance = 0
            
            # pass to childs
            ldis = search(node.left,target,self_distance)
            rdis = search(node.right,target,self_distance)
            
            # try if child find target
            # and update the another child tree
            if self_distance < 0:
                if ldis >= 0: 
                    self_distance = ldis + 1
                    search(node.right,target,self_distance)
                if rdis >= 0: 
                    self_distance = rdis + 1    
                    search(node.left,target,self_distance)
            
            # finally decide distance
            # print(node.val,self_distance)
            if self_distance == K:
                self.res.append(node.val)
                
            return self_distance
        
        search(root,target,-1)
        return self.res
        
```

# solution 2(2 pass)
第一个pass，是遍历一遍，记录前驱，把树改造成graph。  
然后对graph BFS一下