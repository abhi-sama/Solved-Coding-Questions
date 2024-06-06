class Solution {
public:
    int count = 0;
    void dfs(int node, int parent, vector<pair<int, int>> adj[]) {
        for (auto p : adj[node]) {
            int adjacent = p.first;
            if (parent != adjacent) {
                int check = p.second;
                if (check)
                    count++;
                dfs(adjacent, node, adj);
            }
        }
    }
    int minReorder(int n, vector<vector<int>>& connections) {
        vector<pair<int, int>> adj[n];
        for (auto p : connections) {
            adj[p[0]].push_back({p[1], 1}); // real edge
            adj[p[1]].push_back({p[0], 0}); // fake edge
        }
        dfs(0, -1, adj);
        return count;
    }
};