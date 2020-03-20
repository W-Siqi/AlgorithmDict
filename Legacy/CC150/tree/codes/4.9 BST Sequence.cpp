// 待解决！！！！！
// 树的常规操作：遍历打印
// 打印分类树
// STL: 收尾链接哪个效率高？
vector<vector<Node*>> FindSequences(Node* bst){
    vector<vector<Node*>> res;
    if(bst == null){
        vecttor<Node*> onlyEmpty(0);
        res.push_back(onlyEmpty);
        return res;
    }
    auto left = FindSequences(bst->left);
    auto right = FindSequences(bst->right);
    for(int i = 0 ; i < left.size() ; i++){
        for(int j = 0 ; j < left.size() ; j++){
            vecror<Node*> cur1;
            cur.push_back(bst);
            for(auto node:left){
                cur.push_back(node);
            }
            for(auto node:right){
                cur.push_back(node);
            }
            res.push_back(cur1);

            if(left.size() > 0 && right.size() > 0){
                vecror<Node*> cur2;
                cur.push_back(bst);
                for(auto node:right){
                    cur.push_back(node);
                }
                for(auto node:left){
                    ur.push_back(node);
                }
                res.push_back(cur2);
            }
        }
    }
}

