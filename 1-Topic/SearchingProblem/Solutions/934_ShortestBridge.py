# mark遍历过的时机，必须是在加入queue时候，这里把染色延迟到popqueue，那么parent扩张child的‘那一帧’就会重复弄一个节点很多次，然后再递归下去的话后果不堪设想
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # return all pos in the island
        def color(x,y,num,A):
            colored = [(x,y)]
            queue = [(x,y)]
            A[x][y] = num
            while queue:
                # color parent
                topx,topy = queue.pop(0)
                
                # extend child
                neibors = [(topx+1,topy),(topx-1,topy),(topx,topy+1),(topx,topy-1)]
                for neix,neiy in neibors:
                    within = neix >= 0 and neix < len(A) and neiy >= 0 and neiy < len(A[0])
                    if within and A[neix][neiy] == 1:
                        queue.append((neix,neiy))
                        colored.append((neix,neiy))
                        A[neix][neiy] = num
            return colored
        
        queue = []
        for i in range(len(A)):
            colored = False
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    queue.extend(color(i,j,2,A))
                    colored = True
                    break
            if colored:
                break
        # BFS till reach num '1'
        depth = 0
        while queue:
            meetOtherIsland = False
            # extend island
            for i in range(len(queue)):
                x,y = queue.pop(0)
                
                neibors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                for neix,neiy in neibors:
                    within = neix >= 0 and neix < len(A) and neiy >= 0 and neiy < len(A[0])
                    if within and A[neix][neiy] == 1:
                        meetOtherIsland = True
                    elif within and A[neix][neiy] == 0:
                        A[neix][neiy] = 2
                        queue.append((neix,neiy))
                        
            if meetOtherIsland:
                return depth
            else:
                depth += 1
        
        return depth