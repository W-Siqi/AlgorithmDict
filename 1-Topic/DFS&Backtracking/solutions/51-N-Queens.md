# 策略搜索： 棋盘模型-无阶段性策略过程
## 无阶段性的决策过程
这个和字符串匹配的决策过程不一样。字符串用明确的阶段性，而放棋子，我可以先放这个棋子，再放那个棋子，先后顺序无关，只要不冲突就行了。  
因此，这题**一定要引入顺序，否侧会出现重复！**。 比如，棋子一定是从左往右放的
## 特殊之处：正好放N个queen
这题搜索下一步可以放的地方的时候，我是比x坐标大的那一边全部搜了一遍。但这题特殊的是，正好要放N个queen。  
也就是，注定了每一个行放一个。 所以可以规定放第i行就是第n步决策。  
## 如果放小于N个queen 怎么办？
方案1： 第i步就变成放第i个棋子
方案2： 第i步处理第i行的棋子放哪儿，但是又放或不放两个分支（要DP了）
# solution
C++,从1800ms到16ms的百倍优化：  
1. 避免在递归，循环里面放vector.push_back这种昂贵的操作。比如candidates出来了就马上递归了呗，干嘛存起来一起for一遍？ 这样就从1800ms->500ms
2. 最最最要命的，是这里出现了重复子问题。但也无须memo，只要规定顺序，避免重复就行了。
```c++
class Solution {
public:
    vector<vector<string>> res;
    int n;
    
    void dfs(int cur,int mini,vector<string>& chessBoard){
        if(cur >= n){
            // write result
            res.push_back(chessBoard);
            return;
        }
        
        for(int  j = 0; j < n; j++){
            int  i = mini;
            bool valid = true;
            // check [i][j]
            for (int x = 0; x <= i+j; x++){
                int y = i+j-x;
                if(x >= 0 && x < n && y >= 0 && y < n && chessBoard[x][y] == 'Q'){
                    valid = false;
                }
            }
            for(int x = 0; x < n; x++){
                int y = x + (j-i);
                if(x >= 0 && x < n && y >= 0 && y < n && chessBoard[x][y] == 'Q'){
                    valid = false;
                }
            }
            for(int x = 0; x < n ; x++){
                if(chessBoard[x][j] == 'Q'){
                    valid = false;
                    break;
                }
            }

            if(valid){
                chessBoard[i][j] = 'Q';
                dfs(cur+1,i+1,chessBoard);
                chessBoard[i][j] = '.';
            }
        }  
    }
    
    vector<vector<string>> solveNQueens(int n) {
        this->n = n;
        vector<string> emptyBoard(n, std::string(n, '.'));
        dfs(0,0,emptyBoard);
        return res;
    }
};
```