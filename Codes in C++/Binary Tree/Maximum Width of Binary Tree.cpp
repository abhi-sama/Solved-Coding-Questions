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
    int widthOfBinaryTree(TreeNode* root) {
      if(!root)  
        return 0;
      queue<pair<TreeNode*,int>> q;
      int ans=0;
      q.push({root,0});
      while(!q.empty()){
        int qsize=q.size();
        int minm=q.front().second;
        int first,last;
        for(int i=0;i<qsize;i++)
        {   int cur_id=q.front().second -minm;
            TreeNode* temp=q.front().first;
            q.pop();
            if(i==0) first=cur_id;
            if(i==qsize-1) last=cur_id;
            if(temp->left) q.push({temp->left,(long long)cur_id*2+1});
            if(temp->right) q.push({temp->right,(long long)cur_id*2+2});
        }
        ans=max(ans,last-first+1);
      }
      return ans;
    }
};