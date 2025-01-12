vector<int> longestIncreasingSubsequence(int n, vector<int>& nums) {
    vector<int> len(n, 1), hash(n, 1);
    int maxi = 1;
    int lastIndex = 0;
    for (int i = 0; i <= n - 1; i++) {
        hash[i] = i;
        for (int prev = 0; prev <= i - 1; prev++) {
            if (nums[i] > nums[prev] && (len[prev] + 1 > len[i])) {
                len[i] = len[prev] + 1;
                hash[i] = prev;
            }
        }
        if (len[i] > maxi) {
            maxi = len[i];
            lastIndex = i;
        }
    }
    vector<int> lis;
    lis.push_back(nums[lastIndex]);
    while (hash[lastIndex] != lastIndex) {
        lastIndex = hash[lastIndex];
        lis.push_back(nums[lastIndex]);
    }
    reverse(lis.begin(), lis.end());
    return lis;
}


    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> cur(n + 1, 0), next(n + 1, 0);
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int prev_ind = ind - 1; prev_ind >= -1; prev_ind--) {
                int len = 0 + next[prev_ind + 1];
                if (prev_ind == -1 || nums[prev_ind] < nums[ind])
                    len = max(len, 1 + next[ind + 1]);
                cur[prev_ind + 1] = len;
            }
            next = cur;
        }
        return cur[0];
    }



// class Solution {
// public:
//     int lengthOfLIS(vector<int>& nums) {
//         int n = nums.size();
//         vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
//         for (int ind = n - 1; ind >= 0; ind--) {
//             for (int prev_ind = ind - 1; prev_ind >= -1; prev_ind--) {
//                 int len = 0 + dp[ind + 1][prev_ind + 1];
//                 if (prev_ind == -1 || nums[prev_ind] < nums[ind])
//                     len = max(len, 1 + dp[ind + 1][ind + 1]);
//                 dp[ind][prev_ind + 1] = len;
//             }
//         }
//         return dp[0][0];
//     }
// };




// class Solution {
// public:
//     int f(int ind, int prev_ind, vector<int>& nums, int n,
//           vector<vector<int>>& dp) {
//         if (ind == n)
//             return 0;
//         if (dp[ind][prev_ind + 1] != -1)
//             return dp[ind][prev_ind + 1];
//         int len = 0 + f(ind + 1, prev_ind, nums, n, dp);
//         if (prev_ind == -1 || nums[prev_ind] < nums[ind])
//             len = max(len, 1 + f(ind + 1, ind, nums, n, dp));
//         return dp[ind][prev_ind + 1] = len;
//     }

//     int lengthOfLIS(vector<int>& nums) {
//         int n = nums.size();
//         vector<vector<int>> dp(n, vector<int>(n + 1, -1));
//         return f(0, -1, nums, n, dp);
//     }
// };


// class Solution {
// public:
//     int lengthOfLIS(vector<int>& nums) {
//     int n=nums.size();
//     vector<int> len(n,1);
//     for(int i=1;i<n;i++)
//     {
//      for(int j=i-1;j>=0;j--)
//      { 
//          if(nums[i]>nums[j])
//          len[i]=max(len[j]+1,len[i]);
//      }
//     } 
//     return *max_element(len.begin(),len.end());
//     }
// };

