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
    void preOrder(vector<int>& vec, TreeNode* root) {
        if (root != NULL) {
            if (root->left == NULL && root->right == NULL)
                vec.push_back(root->val);
            preOrder(vec, root->left);
            preOrder(vec, root->right);
        }
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> vec1, vec2;
        preOrder(vec1, root1);
        preOrder(vec2, root2);
        return vec1 == vec2;
    }
};