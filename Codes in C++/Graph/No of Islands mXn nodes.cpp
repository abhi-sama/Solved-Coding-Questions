class Solution
{
public:
    void bfs(int row, int col, vector<vector<char>> &grid, vector<vector<int>> &vis)
    {
        vis[row][col] = 1;
        queue<pair<int, int>> q;
        q.push({row, col});
        int m = grid.size();
        int n = grid[0].size();
        while (!q.empty())
        {
            int row = q.front().first;
            int col = q.front().second;
            q.pop();
            for (int delrow = -1; delrow <= 1; delrow++)
                for (int delcol = -1; delcol <= 1; delcol++)
                {
                    int nrow = row + delrow;
                    int ncol = col + delcol;
                    if (nrow >= 0 && nrow < m && ncol >= 0 && ncol < n &&
                        grid[nrow][ncol] == '1' && vis[nrow][ncol] == 0)
                    {
                        vis[nrow][ncol] = 1;
                        q.push({nrow, ncol});
                    }
                }
        }
    }
    // Function to find the number of islands.
    int numIslands(vector<vector<char>> &grid)
    {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> vis(m, vector<int>(n, 0));
        int count = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
            {
                if (vis[i][j] == 0 && grid[i][j] == '1')
                {
                    count++;
                    bfs(i, j, grid, vis);
                }
            }
        return count;
    }
};