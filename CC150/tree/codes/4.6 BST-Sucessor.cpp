// ！！待解决！！！
// BST的一个常见知识点吧
// 注意！比它大的未必是在子节点中！！还要往上找
Node* Sucessor(Node* node){
   if(node->rchild){
       return FindMin(node->rchild);
   }
   else{
       return null;
   }
}

Node* FindMin(Node* node){
    if(node->lChild){
        return FindMin(node->lChild);
    }
    else{
        return node;
    }
}
