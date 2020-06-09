# Graph
这题就是通过信息分析拓扑结构。  
n个节点，n-1条边，而且全相连。  
那么基本就是tree（注意不是二叉树），因此也不带环

# solution
```py
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        m = collections.defaultdict(list)
        for c in connections:
            m[c[0]].append(c)
            m[c[1]].append(c)
            
        destCities = [0]
        res = 0
        visited = set()
        visited.add(0)
        while destCities:
            # print("dest",destCities)
            newDest = []
            for city in destCities:
                for road in m[city]:
                    connectedCity = road[1]
                    if road[0] != city:
                        connectedCity = road[0]
                    # print(connectedCity)
                    if connectedCity not in visited:
                        # new city to add
                        visited.add(connectedCity)
                        newDest.append(connectedCity)
                        if road[0] == city:
                            res += 1
            destCities = newDest
        return res
```