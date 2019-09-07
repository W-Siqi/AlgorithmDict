// BFS嘛, 但是这里就是要标记每一层。
    // 可以用null隔开，不过用计数器标记一下也行（这里就是用计数器）
// STL的list 有点忘了..
vector<List<Node*>> GetLists(Node* root){
    vector<List<Node*>> res;
    queue<Node*> curDepth{root};
    while(curDepth.size() > 0){
        // copy cur to result
        List<Node*> newList;
        for(auto n:curDepth){
            if(n)
                newList.push_back(n);
        }
        res.push_back(newList);

        // switch cur to next depth
        int count = curDepth.size();
        for(int i = 0 ; i < count ; i++){
            auto node = curDepth.front();
            curDepth.pop();

            if(node->lchild)
                node.push(node->lchild);
            if(node->rchild)
                node.push(node->rchild);。
        }
    }

    return res;
}