#include <bits/stdc++.h> 
bool subsetSumToK(int n, int k, vector<int> &arr) {
    vector<bool> prev(k+1,false);
    vector<bool> cur(k+1,false);
    prev[0]=cur[0]=true;
    prev[arr[0]]=true;
    for(int i=1;i<n;i++)
    {
        for(int target=0;target<=k;target++)
        {
            bool not_take=prev[target];
            bool take=false;
            if(arr[i]<=target)
                take=prev[target-arr[i]];
            cur[target]=not_take||take;
        }
        prev=cur;
    }
    return prev[k];
}
// #include <bits/stdc++.h> 
// bool subsetSumToK(int n, int k, vector<int> &arr) {
//     vector<vector<bool>> dp(n,vector<bool>(k+1,false));
//     for(int i=0;i<n;i++)
//         dp[i][0]=true;
//     dp[0][arr[0]]=true;
//     for(int i=1;i<n;i++)
//     {
//         for(int target=0;target<=k;target++)
//         {
//             bool not_take=dp[i-1][target];
//             bool take=false;
//             if(arr[i]<=target)
//                 take=dp[i-1][target-arr[i]];
//             dp[i][target]=not_take||take;
//         }
//     }
//     return dp[n-1][k];
// }