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
    vector<int> preorderTraversal(TreeNode *root)
    {
        vector<int> preorder;
        TreeNode *curr = root;
        while (curr != NULL)
        {
            if (curr->left == NULL)
            {
                preorder.push_back(curr->val);
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
                    preorder.push_back(curr->val);
                    curr = curr->left;
                }
                else
                {
                    prev->right = NULL;
                    curr = curr->right;
                }
            }
        }
        return preorder;
    }
    // vector<int> preorderTraversal(TreeNode *root)
    // vector<int> res;
    // stack<TreeNode*> s;
    // while(root!=NULL||!s.empty())
    // {
    //     while(root!=NULL)
    //     {
    //         res.push_back(root->val);
    //         s.push(root);
    //         root=root->left;
    //     }
    //     root=s.top();
    //     s.pop();
    //     root=root->right;
    // }
    // return res;
    // }
};