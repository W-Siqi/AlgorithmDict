# 策略搜索 - 发现重叠子问题
我一开始的错觉，是以为，这种一步步按顺序做决策分支的，不会出现重叠的子问题，老老实实回溯法就是最优的。  
但是未必！你一个string超过1种分法，就已经代表了：不同的决策可能产生相同的结果（把这个长度的string切分好）。这就意味着会出现重叠子问题。
# 策略搜素DP： bottom up 和 top down
### 一个特例
"aaaaaaaaaaaaaaaaaaaBaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]  
这个例子是真的皮，bottom up会超时，但是top down不会。   
因为i比较小的时候，个数就直接爆炸。但是i大的时候，状态能转移的数量确是0..
### 又发现一个top down的优点
在有的情形，如这种字符匹配。top down计算的状态数目可能会比bottom up 要少很多。

# solution 1 Backtracking(TLE)
```c++
class Solution {
public:
    vector<string> res;
    
    void dfs(string& s, set<string>& wordDict,string santance, string curWord, int pos){
        if(pos >= s.size()){
            if(wordDict.find(curWord)!=wordDict.end()){
                string newSantance = santance == ""? curWord:santance+" "+curWord;
                res.push_back(newSantance);
            }
            return;
        }
        
        string newWord = curWord + s[pos];
        if(wordDict.find(newWord)!=wordDict.end()){
            string newSantance = santance == ""? newWord :santance+" "+newWord;
            dfs(s,wordDict, newSantance,"",pos+1);
        }
        dfs(s,wordDict,santance,newWord,pos+1);
        return;
    }
    
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        set<string> dict;
        for(string s:wordDict){
            dict.insert(s);
        }
        dfs(s,dict,"","",0);
        return res;
    }
};
```

# solution 2 bottom-up DP（TLE）
### 一个可以的优化： 存前缀/后缀序列。   
不一定要trie tree，就是一个dict存每个后缀index可能出现的字母set，每次增加的时候去check一下就ok了。
```c++
class Solution {
public:
    
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<vector<string>> dp(s.size()+1,vector<string>());
        dp[0].push_back("");
        set<string> dict;
        for(string s:wordDict){
            dict.insert(s);
        }
        
        for(int  i = 1; i <= s.size(); i ++){
            string word = "";
            for(int j = i; j >=1; j--){
                word = s[j-1]+word;
                if(dict.find(word)!=dict.end()){
                    for(auto pre:dp[j-1]){
                        string newSantance = pre == ""?word:pre+" "+word;
                        dp[i].push_back(newSantance);
                    }   
                }
            }
        }     
        return dp[s.size()];
    }
};
```