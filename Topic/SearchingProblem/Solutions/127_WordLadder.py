# time limit optimize：
#    instead of using musk, we can just remove the element from the wordList...
# BFS, use queue!! don't use list and switch!
# 'visited' should use set! not list!! because I look up elements frequently 
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if not wordList:
            return 0
        
        if beginWord == endWord:
            return 1
        
        queue = collections.deque([(beginWord,1)])
        visited={(beginWord)}
        
        # init hash dict
        wlen = len(wordList[0])
        dictionary=collections.defaultdict(list)
        for w in wordList:
            for i in range(wlen):
                dictionary[w[0:i]+'*'+w[i+1:wlen]].append(w)
        
        # update candidates until meet endWord or used up all words
        while queue:
            fontw,times = queue.popleft()
            # add candidates to queue
            for i in range(wlen):
                target = fontw[0:i]+'*'+fontw[i+1:wlen]
                mappingList = dictionary[target]  
                for w in mappingList:
                    if w == endWord:
                        return times + 1
                    if w not in visited:
                        queue.append((w,times + 1))
                        visited.add(w)
                        
        
        return 0
        