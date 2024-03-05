/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root)
            return 0;
        int hl=maxDepth(root->left);
        if(hl==-1)
            return -1;
        int hr=maxDepth(root->right);
        if(hr==-1)
            return -1;
        if(abs(hl-hr)>1)
            return -1;
        return 1+ max(hl,hr);
    }
    bool isBalanced(TreeNode* root) {
        return maxDepth(root)!=-1;
    }
};