// 这个和快排的哪个分治法，简直不要太像
Node MinimalTree(vector<int> src){
    return FormTree(src, 0 ,src.size() -1);
}

Node FormTree(vector<int> src, int start, int end){
    if(end < start)
        return null;

    if(start ==  end){
        Node node(src[start]);
        return node;
    }
    else{
        int mid = (start + end)/2;
        Node node(src[start]);
        auto lchild = FormTree(src,start, mid -1);
        auto rchild = FormTree(src,mid + 1, end);
        node.lchild = lchild;
        node.rchild = rchild;
        return node;
    }
}