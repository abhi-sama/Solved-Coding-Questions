 #include<map>
vector<int> bottomView(TreeNode<int> * root){
    queue<pair<TreeNode<int> *,int>> q;
    map<int,int> mpp;
    q.push({root,0});
    while(!q.empty())
    {   TreeNode<int> * node=q.front().first;
        int line=q.front().second;
        q.pop();
        mpp[line]=node->data;
        if(node->left) q.push({node->left,line-1});
        if(node->right) q.push({node->right,line+1});
    }
    vector<int> ans;
    for(auto it:mpp)
        ans.push_back(it.second);
    return ans;
}