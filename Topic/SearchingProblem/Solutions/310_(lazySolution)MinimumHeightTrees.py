class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # organize graph 
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        res = []
        minDepth = n + 1
        
        # calculate depth of every node.
        def calDepth(node, graph):
            visited = {(node)}
            queue = [(node,1)]
            maxDepth = 1
            while queue:
                # pop front
                topNode,topDepth = queue.pop(0)         
                # try add new adjacent nodes
                for adNode in graph[topNode]:
                    if adNode not in visited:
                        visited.add(adNode)
                        queue.append((adNode,topDepth + 1))
                        maxDepth = max(maxDepth,topDepth + 1)
            return maxDepth
            
        for i in range(n):
            depth = calDepth(i,graph)
            if depth == minDepth:
                res.append(i)
            elif depth < minDepth:
                minDepth = depth
                del res[:]
                res.append(i)
                
        return res