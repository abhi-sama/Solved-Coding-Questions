class Solution {
public:
    int coinChange(vector<int>& arr, int T) {
        int n = arr.size();
        vector<int> prev(T+1,0);
        vector<int> cur(T+1,0);
        for (int i = 0; i <= T; i++) {
            if (i % arr[0] == 0)
                prev[i] = i / arr[0];
            else
                prev[i] = 1e9;
        }
        
        for (int ind = 1; ind < n; ind++) {
            for (int target = 0; target <= T; target++) {
                int notTake = prev[target];
                int take = 1e9;
                if (arr[ind] <= target)
                    take = 1 + cur[target - arr[ind]];
                cur[target] = min(notTake, take);
            }
            prev=cur;
        }
        int ans = prev[T];
    
        if (ans >= 1e9)
            return -1;
        
        return ans;
    }
};
// class Solution {
// public:
//     int coinChange(vector<int>& arr, int T) {
//         int n = arr.size();
//         vector<vector<int>> dp(n, vector<int>(T + 1, 0));
//         for (int i = 0; i <= T; i++) {
//             if (i % arr[0] == 0)
//                 dp[0][i] = i / arr[0];
//             else
//                 dp[0][i] = 1e9;
//         }
        
//         for (int ind = 1; ind < n; ind++) {
//             for (int target = 0; target <= T; target++) {
//                 int notTake = dp[ind - 1][target];
//                 int take = 1e9;
//                 if (arr[ind] <= target)
//                     take = 1 + dp[ind][target - arr[ind]];
//                 dp[ind][target] = min(notTake, take);
//             }
//         }
//         int ans = dp[n - 1][T];
    
//         if (ans >= 1e9)
//             return -1;
        
//         return ans;
//     }
// };