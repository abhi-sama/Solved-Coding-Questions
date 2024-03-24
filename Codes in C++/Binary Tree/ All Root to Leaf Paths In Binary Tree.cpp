// bool getPath(node * root, vector < int > & arr, int x) {
//   // if root is NULL
//   // there is no path
//   if (!root)
//     return false;

//   // push the node's value in 'arr'
//   arr.push_back(root -> data);

//   // if it is the required node
//   // return true
//   if (root -> data == x)
//     return true;

//   // else check whether the required node lies
//   // in the left subtree or right subtree of
//   // the current node
//   if (getPath(root -> left, arr, x) ||
//     getPath(root -> right, arr, x))
//     return true;

//   // required node does not lie either in the
//   // left or right subtree of the current node
//   // Thus, remove current node's value from
//   // 'arr'and then return false   
//   arr.pop_back();
//   return false;
// }
void getPath(BinaryTreeNode<int> * root,string temp,vector<string> &ans)
{
    if(!root) return;
    temp+=to_string(root->data)+" ";
    if(!root->left && !root->right)
        ans.push_back(temp.substr(0,temp.size()-1));
    if(root->left) getPath(root->left,temp,ans);
    if(root->right) getPath(root->right,temp,ans);
    return;
}

vector <string> allRootToLeaf(BinaryTreeNode<int> * root) {
    vector<string> ans;
    getPath(root,"",ans);
    return ans;
}