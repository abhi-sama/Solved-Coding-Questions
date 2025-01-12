class Solution {
public:
    bool checkValidString(string s) {
        int min = 0;
        int max = 0;
        for (auto c : s) {
            if (c == '(') {
                min = min + 1;
                max = max + 1;
            } else if (c == ')') {
                min = min - 1;
                max = max - 1;
            } else {
                min = min - 1;
                max = max + 1;
            }
            if (min < 0)
                min = 0;
            if (max < 0)
                return false;
        }
        return (min == 0);
    }
};
// class Solution {
// public:
//     bool helper(string s, int ind, int cnt, vector<vector<int>>& dp) {
//         if (cnt < 0)
//             return false;
//         if (ind == s.length()) {
//             return (cnt == 0);
//         }
//         if (dp[ind][cnt] != -1)
//             return dp[ind][cnt];
//         if (s[ind] == '(') {
//             dp[ind][cnt] = helper(s, ind + 1, cnt + 1, dp);
//             return dp[ind][cnt];
//         }
//         if (s[ind] == ')') {
//             dp[ind][cnt] = helper(s, ind + 1, cnt - 1, dp);
//             return dp[ind][cnt];
//         }
//         bool isValid =
//             (helper(s, ind + 1, cnt - 1, dp) || helper(s, ind + 1, cnt, dp) ||
//              helper(s, ind + 1, cnt + 1, dp));
//         dp[ind][cnt] = isValid;
//         return dp[ind][cnt];
//     }
//     bool checkValidString(string s) {
//         int n = s.length();
//         vector<vector<int>> dp(n, vector<int>(n, -1));
//         return helper(s, 0, 0, dp);
//     }
// };
class Solution {
public:
    bool helper(string s, int ind, int cnt, vector<vector<int>>& dp) {
        if (cnt < 0)
            return false;
        if (ind == s.length()) {
            return (cnt == 0);
        }
        if (dp[ind][cnt] != -1)
            return dp[ind][cnt];
        if (s[ind] == '(') {
            dp[ind][cnt] = helper(s, ind + 1, cnt + 1, dp);
            return dp[ind][cnt];
        }
        if (s[ind] == ')') {
            dp[ind][cnt] = helper(s, ind + 1, cnt - 1, dp);
            return dp[ind][cnt];
        }
        bool isValid =
            (helper(s, ind + 1, cnt - 1, dp) || helper(s, ind + 1, cnt, dp) ||
             helper(s, ind + 1, cnt + 1, dp));
        dp[ind][cnt] = isValid;
        return dp[ind][cnt];
    }
    bool checkValidString(string s) {
        int n = s.length();
        vector<vector<bool>> dp(n + 1, vector<bool>(n + 1, false));
        dp[n][0] = true;
        for (int ind = n - 1; ind >= 0; ind--) {
            bool isValid = false;
            for (int cnt = 0; cnt <= n - 1; cnt++) {
                if (s[ind] == '(') {
                    if (cnt + 1 <= n)
                        isValid = dp[ind + 1][cnt + 1];
                } else if (s[ind] == ')') {
                    if (cnt > 0)
                        isValid = dp[ind + 1][cnt - 1];
                } else {
                    bool takeAsEmpty = dp[ind + 1][cnt];
                    bool takeAsOpen =
                        (cnt + 1 <= n) ? dp[ind + 1][cnt + 1] : false;
                    bool takeAsClose = (cnt > 0) ? dp[ind + 1][cnt - 1] : false;
                    isValid = takeAsEmpty || takeAsOpen || takeAsClose;
                }
                dp[ind][cnt] = isValid;
            }
        }
        return dp[0][0];
    }
};