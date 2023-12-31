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
class Solution
{
public:
    vector<int> inorderTraversal(TreeNode *root)
    {
        vector<int> inorder;
        TreeNode *curr = root;
        while (curr != NULL)
        {
            if (curr->left == NULL)
            {
                inorder.push_back(curr->val);
                curr = curr->right;
            }
            else
            {
                TreeNode *prev = curr->left;
                while (prev->right && prev->right != curr)
                    prev = prev->right;
                if (prev->right == NULL)
                {
                    prev->right = curr;
                    curr = curr->left;
                }
                else
                {
                    prev->right = NULL;
                    inorder.push_back(curr->val);
                    curr = curr->right;
                }
            }
        }
        return inorder;
    }
    /* vector<int> inorderTraversal(TreeNode* root) {
     vector<int> res;
     stack<TreeNode*> s;
     while(root!=NULL||!s.empty())
     {
         while(root!=NULL)
         {
             s.push(root);
             root=root->left;
         }
         root=s.top();
         s.pop();
         res.push_back(root->val);
         root=root->right;
     }
     return res;
     }*/
    /*public:
        vector<int> inorderTraversal(TreeNode* root) {
            vector<int> nodes;
            inorder(root, nodes);
            return nodes;
        }
    private:
        void inorder(TreeNode* root, vector<int>& nodes) {
            if (!root) {
                return;
            }
            inorder(root -> left, nodes);
            nodes.push_back(root -> val);
            inorder(root -> right, nodes);
        }*/
};