void left(Node* root,int level,vector<int> &res)
{
    if(root==NULL)return;
    if(level==res.size())res.push_back(root->data);
    left(root->left,level+1,res);
    left(root->right,level+1,res);
}
//Function to return a list containing elements of left view of the binary tree.
vector<int> leftView(Node *root)
{
   vector<int> res;
   left(root,0,res);
   return res;
}