class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m = maze.size();
        int n = maze[0].size();
        vector<vector<int>> vis(m, vector<int>(n, 0));
        int dr[] = {-1, 0, +1, 0};
        int dc[] = {0, +1, 0, -1};
        queue<pair<pair<int, int>, int>> q;
        q.push({{entrance[0], entrance[1]}, 0});
        vis[entrance[0]][entrance[1]] = 1;
        while (!q.empty()) {
            int r = q.front().first.first;
            int c = q.front().first.second;
            int s = q.front().second;
            q.pop();
            if (((r == 0) || (r == m - 1) || (c == 0) || (c == n - 1)) &&
                (r != entrance[0] || c != entrance[1]))
                return s;
            for (int i = 0; i < 4; i++) {
                int nrow = dr[i] + r;
                int ncol = dc[i] + c;
                if (nrow >= 0 && nrow < m && ncol >= 0 && ncol < n &&
                    maze[nrow][ncol] == '.' && vis[nrow][ncol] == 0) {
                    vis[nrow][ncol] = 1;
                    q.push({{nrow, ncol}, s + 1});
                }
            }
        }
        return -1;
    }
};