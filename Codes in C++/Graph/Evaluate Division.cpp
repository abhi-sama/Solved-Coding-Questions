class Solution {
public:
    void dfs(string src, string dest,
             unordered_map<string, vector<pair<string, double>>>& adj,
             double product, double& ans, unordered_set<string>& vis) {
        if (vis.find(src) != vis.end())
            return;
        vis.insert(src);
        if (src == dest)
            ans = product;
        for (auto& p : adj[src]) {
            string v = p.first;
            double val = p.second;
            dfs(v, dest, adj, product * val, ans, vis);
        }
    }
    vector<double> calcEquation(vector<vector<string>>& equations,
                                vector<double>& values,
                                vector<vector<string>>& queries) {
        int n = equations.size();
        unordered_map<string, vector<pair<string, double>>> adj;
        for (int i = 0; i < n; i++) {
            string u = equations[i][0];
            string v = equations[i][1];
            double val = values[i];
            adj[u].push_back({v, val});
            adj[v].push_back({u, 1.0 / val});
        }
        vector<double> result;
        for (auto query : queries) {
            string src = query[0];
            string dest = query[1];
            double ans = -1;
            double product = 1.0;
            if (adj.find(src) != adj.end()) {
                unordered_set<string> vis;
                dfs(src, dest, adj, product, ans, vis);
            }
            result.push_back(ans);
        }
        return result;
    }
};