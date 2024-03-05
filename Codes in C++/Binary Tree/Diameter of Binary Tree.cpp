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
 */ﬁ
class Solution {
public:
    int maxDepth(TreeNode* root,int &diameter) {
        if(!root)
            return 0;
        int hl=maxDepth(root->left,diameter);
        int hr=maxDepth(root->right,diameter);
        diameter=max(diameter,hl+hr);
        return 1+ max(hl,hr);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter=0;
        maxDepth(root,diameter);
        return diameter;
    }
};