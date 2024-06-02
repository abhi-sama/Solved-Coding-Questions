class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        map<vector<int>, int> mpp;
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; i++) {
            mpp[grid[i]]++;
        }
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            vector<int> temp;
            for (int j = 0; j < m; j++) {
                temp.push_back(grid[j][i]);
            }
            if (mpp.find(temp) != mpp.end())
                cnt += mpp[temp];
        }
        return cnt;
    }
};