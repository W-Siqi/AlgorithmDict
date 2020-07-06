# 后序遍历

```c++
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> nodeStack;
        stack<int> signStack;
        vector<int> res;
        
        TreeNode* cur = root;
        int sign = 0;
        while(cur != nullptr || nodeStack.size() > 0){
            if(cur == nullptr){
                cur = nodeStack.top();
                sign = signStack.top();
                nodeStack.pop();
                signStack.pop();
            }    
            
     
            if(sign == 0){
                // 第1次遇见，先push，换left
                nodeStack.push(cur);
                signStack.push(sign+1);
                cur = cur->left;
                sign = 0;
            }
            else if(sign == 1){
                // 第2次遇见，还是push，换right
                nodeStack.push(cur);
                signStack.push(sign+1);
                cur = cur->right;
                sign = 0;
            }
            else{
                // 这都第3次遇见了，成全他，push values了，并且放置为nullptr
                res.push_back(cur->val);
                cur = nullptr;
            }
        }
        
        return res;
    }
};
```