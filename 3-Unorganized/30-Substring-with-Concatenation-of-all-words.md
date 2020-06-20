```py
# bug log: branch leak when 'end' reach out of index 
# bug log: when 'end' reach end, start no update then dead loop
# bug: too many palce , to many branches, and some branch forget to check the count and uodate result
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        
        def find(offset,s,words_max,words_sum):
            wlen = len(words[0])
            words_pos= {}
            start,end = offset,offset
            res = []
            count = 0
            while start + wlen <= len(s) and end + wlen <= len(s):     
                while end + wlen <= len(s):
                    # fetch next word
                    w = s[end:end+wlen]
                    w_pos = end
                    end += wlen
                    
                    if w in words_max:
                        if w not in words_pos:
                            # first add
                            words_pos[w] = [w_pos]
                            count += 1
                            if count == words_sum:
                                res.append(start) 
                        elif len(words_pos[w]) < words_max[w]:
                            # still can append
                            words_pos[w].append(w_pos)
                            count += 1
                            if count == words_sum:
                                res.append(start) 
                        else:
                            # reboot: meet repeat                       
                            words_pos[w].append(w_pos)
                            count = 0
                            start = words_pos[w][0]+wlen
                            # clear the previous
                            for key,val in words_pos.items():
                                remained = []
                                for pos in val:
                                    if pos >= start:
                                        remained.append(pos)
                                words_pos[key] = remained
                                count += len(remained)
                            if count == words_sum:
                                res.append(start) 
                            break
                    else:
                        # reboot:meet gap                  
                        start = end 
                        words_pos.clear()
                        count = 0
                        break   
                        
            return res
        
        wlen = len(words[0])
        res = [] 
        
        words_max = {}
        for w in words:
            if w not in words_max:
                words_max[w] = 1
            else:
                words_max[w] += 1
        for i in range(wlen):
            res += find(i,s,words_max,len(words))
        return respy

```