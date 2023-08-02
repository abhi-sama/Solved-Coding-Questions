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
    vector<int> postorderTraversal(TreeNode *root)
    {
        vector<int> res;
        TreeNode *cur = root;
        TreeNode *temp = NULL;
        stack<TreeNode *> s;
        while (cur != NULL || !s.empty())
        {
            if (cur != NULL)
            {
                s.push(cur);
                cur = cur->left;
            }
            else
            {
                temp = s.top()->right;
                if (temp == NULL)
                {
                    temp = s.top();
                    s.pop();
                    res.push_back(temp->val);
                    while (!s.empty() && temp == s.top()->right)
                    {
                        temp = s.top();
                        s.pop();
                        res.push_back(temp->val);
                    }
                }
                else
                    cur = temp;
            }
        }
        return res;
    }
    // vector<int> postorderTraversal(TreeNode* root) {
    //     stack<TreeNode*> s1;
    //     stack<TreeNode*> s2;
    //     vector<int> res;
    //     if(root==NULL)return res;
    //     s1.push(root);
    //     while(!s1.empty())
    //     {TreeNode* temp=s1.top();
    //      s1.pop();
    //      s2.push(temp);
    //      if(temp->left)
    //         s1.push(temp->left);
    //      if(temp->right)
    //         s1.push(temp->right);
    //     }
    //     while(!s2.empty())
    //     {
    //         res.push_back(s2.top()->val);
    //         s2.pop();
    //     }
    //     return res;
    // }
};