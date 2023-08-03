class Solution {
public:
    bool isCycle(int src,vector<vector<int>>& adj,vector<int>& vis){
        vis[src]=1;
        queue<pair<int,int>> q;
        q.push({src,-1});
        while(!q.empty())
        {
         int node=q.front().first;
         int parent=q.front().second;
         q.pop();
         for(auto adjacent:adj[node])
         {
             if(!vis[adjacent])
                {
                    vis[adjacent]=1;
                    q.push({adjacent,node});
                }
            else if(parent!=adjacent)
            {
                return true;
            }
         }
        }
        return false;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    int v=numCourses;
    vector<int> vis(v,0);
    for(int i=0;i<v;i++)
    {   if(!vis[i])
        if(isCycle(i,prerequisites,vis)) 
            return false;
    }
    return true;
    }
};