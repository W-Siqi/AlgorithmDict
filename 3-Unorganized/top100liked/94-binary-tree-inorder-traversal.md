# 中序非递归
核心： 每个节点会经历2次，第一个是在cur指针，被push进去，第二次是从栈取出来，这个时候left已经完了，read之后转向right child  

# solution
cur + stack 是比较简洁的写法：
```c++
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> s;
        TreeNode* cur = root;
        // 递归退出条件： cur和stack都没货了
        while(cur != nullptr || s.size() > 0){
            if(cur != nullptr){
                // 说明还有左child
                s.push(cur);
                cur = cur->left;
            }
            else{
                // 取出来的top，说明他的左边已经遍历完了，所以先存val
                cur = s.top();
                s.pop();
                res.push_back(cur->val);
                // 然后cur移到动到right
                cur = cur->right;
            }
        }
        return res;
    }
};
```