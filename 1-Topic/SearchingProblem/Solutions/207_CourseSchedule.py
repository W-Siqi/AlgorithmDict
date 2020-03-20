# key idea: new activated element may activate more elements
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # merge prerequisites
        preDict = collections.defaultdict(list)
        nextDict = collections.defaultdict(list)
        for pair in prerequisites:
            preDict[pair[0]].append(pair[1])
            nextDict[pair[1]].append(pair[0])
        # take courses have no prerequisite first
        isTaken = []
        for i in range(numCourses):
            isTaken.append(True)
        for pair in prerequisites:
            isTaken[pair[0]] = False
        
        # keep adding courses by BFS
        takenCount = 0
        queue = []
        for i in range(numCourses):
            if isTaken[i]:
                queue.append(i)
                takenCount += 1
        
        while queue:
            # unlock the untoken courses based on the queue top
            top = queue.pop(0)
            for nextCor in nextDict[top]:
                if isTaken[nextCor]:
                    continue
                
                # check all prequisites of this course
                canTake = True  
                for preCor in preDict[nextCor]:
                    if not isTaken[preCor]:
                        canTake = False
                        break
                
                if canTake:
                    takenCount += 1
                    isTaken[nextCor] = True
                    queue.append(nextCor)
        
        if takenCount == numCourses:
            return True
        else:
            return False