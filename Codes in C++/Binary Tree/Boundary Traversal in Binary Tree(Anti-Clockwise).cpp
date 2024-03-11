/************************************************************

    Following is the Binary Tree node structure:

    template <typename T>
    class TreeNode
    {
    public:
        T data;
        TreeNode<T> *left;
        TreeNode<T> *right;

        TreeNode(T data)
        {
            this -> data = data;
            left = NULL;
            right = NULL;
        }

        ~TreeNode()
        {
            if(left)
                delete left;
            if(right)
                delete right;
        }
    };

************************************************************/
bool isLeaf(TreeNode<int> *root)
{
    return !root->left && !root->right;
}
void addLeftBoundary(TreeNode<int> *root,vector<int> &res)
{
    TreeNode<int> * cur=root->left;
    while(cur)
    {   if(!isLeaf(cur))
            res.push_back(cur->data);
        if(cur->left)
            cur=cur->left;
        else 
            cur=cur->right;    
    }
}
void addBottomBoundary(TreeNode<int> *root,vector<int> &res)
{
    if(isLeaf(root))
        res.push_back(root->data);
    if(root->left)addBottomBoundary(root->left,res);
    if(root->right)addBottomBoundary(root->right,res);
}
void addRightBoundary(TreeNode<int> *root,vector<int> &res)
{
    TreeNode<int> * cur=root->right;
    vector<int> temp;
    while(cur)
    {   if(!isLeaf(cur))
            temp.push_back(cur->data);
        if(cur->right)
            cur=cur->right;
        else 
            cur=cur->left;    
    }
    for(int i=temp.size()-1;i>=0;i--)
        res.push_back(temp[i]);
}
vector<int> traverseBoundary(TreeNode<int> *root)
{
    vector<int> res;
    if(!root)
        return res;
    if(!isLeaf(root))
        res.push_back(root->data);
    addLeftBoundary(root,res);
    addBottomBoundary(root,res);
    addRightBoundary(root,res);  
    return res;
}
