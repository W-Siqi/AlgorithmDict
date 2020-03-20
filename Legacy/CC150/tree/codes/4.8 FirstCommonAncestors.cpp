// !!待解决！！
// 还是个自底向上的东西
// 这里就是需要一个short cut 做返回值，我们可以用全局变量或者穿引用实现
Node* FindCommonAncestor(Node* root, Node* n1, Node* n2){
    Node* res = null;
    FindCommonAncestor(root,n1,n2,res);
    return res;
}

int FindCommonAncestor(Node* root, Node* n1, Node* n2, Node* & res){
    if(root == null){
        return 0;
    }

    int lCount = FindCommonAncestor(root->lchild, n1,n2,res);
    int rCount = FindCommonAncestor(root->rchild,n1,n2,res);
    int selfCount = 0;
    if(root == n1 || root == n2)
        selfCount = 1;
    
    int sumCount = lCount + rCount + selfCount;

    if(sumCount == 2 && res == null){
        res = root;
    }

    return  sumCount;
}