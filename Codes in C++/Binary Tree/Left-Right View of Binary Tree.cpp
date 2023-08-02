void left(Node* root,int level,vector<int> &res)
{
    if(root==NULL)return;
    if(level==res.size())res.push_back(root->data);
    left(root->left,level+1,res);
    left(root->right,level+1,res);
}
//Function to return a list containing elements of left view of the binary tree.
vector<int> leftView(Node *root)
{
   vector<int> res;
   left(root,0,res);
   return res;
}

// vector<int> leftView(Node *root)
//     {
//        // Your Code here
//          vector<int> result;
//     if (!root)
//         return result;
//     queue<Node*> levelQueue;
//     levelQueue.push(root); 
//     while (!levelQueue.empty()) {
//         int levelSize = levelQueue.size(); 
//               // Traverse all nodes in the current level and keep track of the leftmost node's value
//                int leftmostValue;
//           for (int i = 0; i < levelSize; ++i) {

//                  Node* node = levelQueue.front(); 
//                  levelQueue.pop(); 
//                  leftmostValue = node-> data;
            
//                  if(i==0) result.push_back(leftmostValue); 

//                 if (node->left) 
//                      levelQueue.push(node->left);
//                 if (node->right) // same as left
//                      levelQueue.push(node->right);
//         }
//     }
//     return result;
//     };