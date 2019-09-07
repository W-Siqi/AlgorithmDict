// 还是那个，二叉树的遍历的时候，short cut
// tree的公共节点，和链表一样，只要有一个根节点一样，剩下的就全部是雷同，一模一样！
// C++知识：这里比较节点，是比较指针本身还是指针所指的值？
bool IsSubTree(Node* t1, Node* t2){
    return Exist(t1,t2);
}

bool Exist(Node* target, Node* root){
    if(root == null)
        return false;
    
    if(*root == *target)
        return true;
    else{
        return (Exist(root->lchild) || Exist(root->rchild));
    }
}
