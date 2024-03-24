void chnageTree(Node* root)
{
    if(root==NULL) return;
    int child=0;
    if(root->left)
        child+=root->left->data;
    if(root->right)
        child+=root->right->data;
    if(child>=root->data) root->data=child;
    else{
        if(root->left) root->left->data=root->data;
        if(root->right) root->right->data=root->data;
    }
    chnageTree(root->left);
    chnageTree(root->right);
    if tot=0;
    if(root->left) tot+=root->left->data;
    if(root->right) tot+=root->right->data;
    if(root->left || root->right) root->data=tot;
}


// bool isParentSum(Node *root)
// {
//     // Base case: If the root is NULL or it is a leaf node, it satisfies the Parent Sum property
//     if (root == NULL || (root->left == NULL && root->right == NULL))
//     {
//         return true;
//     }

//     // Subtract the values of the left and right child from the current node's value
//     if (root->left)
//     {
//         root->data -= root->left->data;
//     }
//     if (root->right)
//     {
//         root->data -= root->right->data;
//     }

//     // Check if the current node's value is equal to the sum of its children's values
//     if (root->data == 0)
//     {
//         // Recursively check the Parent Sum property for the left and right subtrees
//         return isParentSum(root->left) && isParentSum(root->right);
//     }

//     // If the current node's value is not equal to the sum of its children's values, 
//     // it does not satisfy the Parent Sum property
//     return false;
// }