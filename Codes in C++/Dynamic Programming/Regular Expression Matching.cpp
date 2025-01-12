class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.length(), m = p.length();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        
        dp[n][m] = true;  
        
        for (int i = n; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                bool first_char_matched = (i < n && (s[i] == p[j] || p[j] == '.'));
                
                if (j + 1 < m && p[j + 1] == '*') {
                    dp[i][j] = dp[i][j + 2] || (first_char_matched && dp[i + 1][j]);
                } else {
                    dp[i][j] = first_char_matched && dp[i + 1][j + 1];
                }
            }
        }
        
        return dp[0][0];
    }
};
// class Solution {
// public:
//     bool solve(int i, int j, string s, string p, vector<vector<int>>& dp) {
//         if (j == p.length()) {
//             return i == s.length();
//         }
//         if (dp[i][j] != -1)
//             return dp[i][j];
//         bool first_char_matched = false;
//         if (i < s.length() && (s[i] == p[j] || p[j] == '.')) {
//             first_char_matched = true;
//         }
//         if (j + 1 < p.length() && p[j + 1] == '*') {
//             bool not_take = solve(i, j + 2, s, p, dp);
//             bool take = first_char_matched && solve(i + 1, j, s, p, dp);
//             return dp[i][j] = not_take || take;
//         }
//         return dp[i][j] = first_char_matched && solve(i + 1, j + 1, s, p, dp);
//     }
//     bool isMatch(string s, string p) {
//         int n = s.length(), m = p.length();
//         vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1));
//         return solve(0, 0, s, p, dp);
//     }
// };