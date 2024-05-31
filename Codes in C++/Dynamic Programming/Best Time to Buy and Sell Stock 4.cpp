// A different Approach dp[N][4] 

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        vector<int> after(2 * k + 1);
        vector<int> curr(2 * k + 1);
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int tranNo = 2 * k - 1; tranNo >= 0; tranNo--) {
                if (tranNo % 2 == 0) {
                    curr[tranNo] = max(-prices[ind] + after[tranNo + 1],
                                       0 + after[tranNo]);
                } else {
                    curr[tranNo] =
                        max(prices[ind] + after[tranNo + 1], 0 + after[tranNo]);
                }
            }
            after = curr;
        }
        return after[0];
    }
};


// class Solution {
// public:
//     int maxProfit(int k, vector<int>& prices) {
//         int n = prices.size();
//         vector<vector<int>> dp(n + 1, vector<int>(2 * k + 1));
//         for (int ind = n - 1; ind >= 0; ind--) {
//             for (int tranNo = 2 * k - 1; tranNo >= 0; tranNo--) {
//                 if (tranNo % 2 == 0) {
//                     dp[ind][tranNo] =
//                         max(-prices[ind] + dp[ind + 1][tranNo + 1],
//                             0 + dp[ind + 1][tranNo]);
//                 } else {
//                     dp[ind][tranNo] = max(prices[ind] + dp[ind + 1][tranNo + 1],
//                                           0 + dp[ind + 1][tranNo]);
//                 }
//             }
//         }
//         return dp[0][0];
//     }
// };





// class Solution {
// public:
//     int maxProfit(int k, vector<int>& prices) {
//         int n = prices.size();
//         vector<vector<int>> after(2, vector<int>(k + 1, 0));
//         vector<vector<int>> curr(2, vector<int>(k + 1, 0));
//         for (int ind = n - 1; ind >= 0; ind--) {
//             for (int buy = 0; buy <= 1; buy++) {
//                 for (int cap = 1; cap <= k; cap++) {
//                     if (buy) {
//                         curr[buy][cap] = max(-prices[ind] + after[0][cap],
//                                              0 + after[1][cap]);
//                     } else {
//                         curr[buy][cap] = max(prices[ind] + after[1][cap - 1],
//                                              0 + after[0][cap]);
//                     }
//                 }
//             }
//             after = curr;
//         }
//         return after[1][k];
//     }
// };