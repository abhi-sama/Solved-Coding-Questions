// Space Optimised
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        vector<int> front2(2, 0);
        vector<int> front1(2, 0);
        vector<int> curr(2, 0);
        for (int ind = n - 1; ind >= 0; ind--) {
            curr[1] = max(-prices[ind] + front1[0], 0 + front1[1]);
            curr[0] = max(prices[ind] + front2[1], 0 + front1[0]);
            front2=front1;
            front1=curr;
        }
        return front1[1];
    }
}; 


// class Solution {
// public:
//     int maxProfit(vector<int>& prices) {
//         int n = prices.size();
//         vector<vector<int>> dp(n + 2, vector<int>(2, 0));
//         for (int ind = n - 1; ind >= 0; ind--) {
//             // for(int buy=0;buy<=1;buy++)
//             // {
//             //     if(buy)
//             //     {
//             //         dp[ind][buy]=max(-prices[ind]+dp[ind+1][0],0+dp[ind+1][1]);
//             //     }
//             //     else{
//             //         dp[ind][buy]=max(prices[ind]+dp[ind+2][1],0+dp[ind+1][0]);
//             //     }
//             // }

//             dp[ind][1] = max(-prices[ind] + dp[ind + 1][0], 0 + dp[ind + 1][1]);
//             dp[ind][0] = max(prices[ind] + dp[ind + 2][1], 0 + dp[ind + 1][0]);
//         }
//         return dp[0][1];
//     }
// };