# 前序非递归
这个最简单：
- 从栈取出
- 访问自己  
- pushChilds（注意栈的顺序是反的，push也要反着push）
# solution1
```c++
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> s;
        s.push(root);
        while(s.size() > 0){
            TreeNode* top = s.top();
            s.pop();
            if(top!=nullptr){
                res.push_back(top->val);
                s.push(top->right);
                s.push(top->left);
            }
        }
        return res;
    }
};
```