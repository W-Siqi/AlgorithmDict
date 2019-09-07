// 知识点：如何自己写一个 随机数
// 知识点： 返回一个指针，会？？？
// 又是那个问题，遍历是的时候shortcut的方法
Node* GetRandomNode(Node* root){
    int sum = NodesNum(root);
    int choosed = Random(0, sum - 1);
    return GetByCounter(root, choosed);
}

int Random(int min, int max){

}

int NodesNum(Node* root){
    if(root == null)
        return 0;
    
    return root + NodesNum(root->lchild) + NodesNum(root->rchild);
}

Node* GetByCounter(Node* root, int& count){
    if(root == null)
        return null;

    count--;
    if(count < 0)
        return root;  

    auto node = GetByCounter(root->lchild,count);
    if(!node)
        return node;
    else
        return GetByCounter(root->rchild,count);
}