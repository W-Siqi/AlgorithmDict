// 和4.4一样自底向上check，递归流程记在心！
bool ValidBST(Node* root, int & min, int &max){
    if(root == null){
        min = INT_MAX;
        max = INT_MIN;
        return true;
    }
    int lmin,lmax,rmin,rmax;
    auto lcheck = ValidBST(root->lchild, lmin,lmax);
    auto rcheck = ValidBST(root->rchild, rmin,rmax);
    min = Min(lmin, rmin);
    max = Max(lmax, rmax);

    if(!lcheck || !rcheck){
        return false;
    }
    if(root->lchild && lmax > root->value){
        return false;
    }
    if(root-<rchild && rmin < root->value){
        return false;
    }
    return true;
}