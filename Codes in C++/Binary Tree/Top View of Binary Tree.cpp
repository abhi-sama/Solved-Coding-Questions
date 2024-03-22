vector<int> getTopView(TreeNode<int> *root)
{   vector<int> ans;
    if(!root) return ans;
   map<int,int> mpp;
   queue<pair<TreeNode<int>*,int >> q;
   q.push({root,0});
   while(!q.empty())
    {   auto p=q.front();
        q.pop();
        TreeNode<int> * temp=p.first;
         int line=p.second;
        if(mpp.find(line)==mpp.end()) mpp[line]=temp->data;
           if(temp->left){
            q.push({temp->left,line-1});
        }
        if(temp->right){
            q.push({temp->right,line+1});
        } 
   }
   for(auto it:mpp)
   ans.push_back(it.second);
   return ans;
}