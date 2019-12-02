// WRONG ANSWER1: forget the edge case that K == 0， which means my algorithem doesn't work if there is no chance to turn 0 to 1
// WRONG ANSWER2:  I update the max value within the while loop, but when end pointer meet the last index and break from the loop
//                 this round will not be recorded. 
class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int start = 0, end = 0;
        int remainK = K;
        queue<int> indexK;
        int res = 0;
        
        while(end < A.size()){
            if(A[end] == 1){
            // end meet 1
                end++;
                continue;
            }
            else{
            // end meet 0
                if(remainK > 0){
                    // still have chances, keep going
                    indexK.push(end);
                    remainK--;
                }
                else{
                    // no chance, adjust pointers and restart
                    res = max(res,end -start);
                    if(K == 0)
                        // special case, K == 0, cannot find the earliest positon of the index.
                        start = end + 1;
                    else{
                        // otherwise, start accroding to the earliest positon of the index.
                        start = indexK.front() + 1;
                        indexK.pop();
                        indexK.push(end); 
                    }
                }
                end++;
            }
        }
        
        // don't forgot to record the result after end pointer meet the last index!
        res = max(res,end -start);
        return res;
    }
};