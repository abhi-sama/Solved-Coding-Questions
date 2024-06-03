/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    void preOrder(int& nice, int prev, TreeNode* root) {
        if (root != NULL) {
            if (root->val >= prev) {
                nice++;
                prev = root->val;
            }
            preOrder(nice, prev, root->left);
            preOrder(nice, prev, root->right);
        }
    }
    int goodNodes(TreeNode* root) {
        int nice = 0;
        int prev = INT_MIN;
        preOrder(nice, prev, root);
        return nice;
    }
};