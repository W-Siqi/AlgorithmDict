// WRONG ANSWER1: forget to record the situation when end == start + 1 and start == A.size() - 1
// WRONF ANSWER2: pay attention to the ++ -- of the indicator in while loop, 
//                especiallay there are several tracks 
class Solution {
public:
    int subarraysWithKDistinct(vector<int>& A, int K) {
        int curNum = 0;
        unordered_map<int,int> m;// number, size
        int start = 0, end = 1;
        // init
        m[A[start]]++;
        curNum = 1;
        int res = 0;
        while(start < A.size()){
            if(curNum == K)
                res++;
            
            while(end < A.size()){
                // add A[end] to cur subarray
                if(m.count(A[end]) > 0 && m[A[end]] > 0){
                    // existed, add count
                    m[A[end]]++;
                }
                else{
                    // unexisted, recourd diff num
                    curNum++;
                    m[A[end]]++;
                }   
                
                end++;
                
                if(curNum == K){
                    res++;
                }
                else if(curNum < K){
                }
                else if(curNum > K){
                    break;
                }  
            } 
          
      
            m[A[start]]--;
            if(m[A[start]] == 0)
                curNum--;
            start++;   
            
            while(end >= start + 2 && curNum >= K){
                end--;
                m[A[end]]--;
                curNum -= m[A[end]] == 0? 1:0;
            }                
        }
        
        return res;
    }
};