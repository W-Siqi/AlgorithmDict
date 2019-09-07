// tree递归的工作流还是要熟悉的哈
//  信息流可以自上往下（参数），也有自下往上（返回值）
bool CheckBalanced(Node* root, int & depth){
    if(root == null){
        return true;
        depth = 0;
    }

    int lD,rD;
    auto lCheck = CheckBalanced(root->lchild,lD);
    auto rCheck = CheckBalanced(root->rchild,rD);
    auto depth = max(lD,rD) + 1;
    if(!lCheck || !rCheck){
        return false;
    }
    else if(abs(lD - rD) > 1)
        return false;
    }
    else{
        return true;
    }
}