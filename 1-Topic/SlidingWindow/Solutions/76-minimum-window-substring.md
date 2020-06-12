# 找最优subarray
唯一注意的就是怎么记录当前的subarray的状态，  
这种情况一定要注意Duplication！
# solution
```py
class Solution(object):
    def minWindow(self, s, t):
        if t =="":return ""

        needs,remain = collections.Counter(t),len(t)
        resi,resj = -float("inf"),float("inf")
        start = 0
        for i,char in enumerate(s):
            if needs[char] > 0:
                remain -= 1
            needs[char] -= 1
            
            while start <= i and remain == 0:
                if i - start < resj - resi:
                    resi,resj = start,i+1
                needs[s[start]] += 1
                if needs[s[start]] > 0:
                    remain = 1
                start += 1
        if resj <= len(s):
            return s[resi:resj]
        else:
            return ""
```

# solution 2 预过滤：一个花里胡哨的技巧
因为遍历的元素我们毫不关心，那就把它过滤掉。  
这在频繁查找里面倒是很有用，只是这题sliding window本身就是O（N）的，这个是不太必要的。
```py
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        dict_t = Counter(t)

        required = len(dict_t)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]

                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    

            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
```