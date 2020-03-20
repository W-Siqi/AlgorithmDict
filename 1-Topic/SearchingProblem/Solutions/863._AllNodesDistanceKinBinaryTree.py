# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def fillGraph(root,graph):
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                fillGraph(root.left,graph)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                fillGraph(root.right,graph)
        
        graph = collections.defaultdict(list)
        fillGraph(root,graph)
        
        # graph BFS
        visited = {target.val}
        queue = [target.val]
        curDepth = 0
        while queue and curDepth < K:
            # switch to next layer
            for i in range(len(queue)):
                top =  queue.pop(0)
                for nei in graph[top]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            
            curDepth += 1
        
        return queue