#include <bits/stdc++.h> 
int mod=(1e9+7);
int findWays(vector<int> &num, int tar){
     int n = num.size();
    vector<vector<int>> dp(n,vector<int>(tar+1,0));
    if(num[0] == 0) dp[0][0] =2;  // 2 cases -pick and not pick
    else dp[0][0] = 1;  // 1 case - not pick
    
    if(num[0]!=0 && num[0]<=tar) dp[0][num[0]] = 1;  // 1 case -pick
    
    for(int ind = 1; ind<n; ind++){
        for(int target= 0; target<=tar; target++){
            
            int notTaken = dp[ind-1][target];
    
            int taken = 0;
                if(num[ind]<=target)
                    taken = dp[ind-1][target-num[ind]];
        
            dp[ind][target]= (notTaken + taken)%mod;
        }
    }
    return dp[n-1][tar];
}

int countPartitions(int n, int d, vector<int> &arr) {
    int total_sum=0;
    for(int x:arr) total_sum+=x;
    vector<vector<int>> dp(n,vector<int>(total_sum+1,-1));
    if(total_sum-d<0||(total_sum-d)%2) return false;
    return findWays(arr,(total_sum-d)/2);
}

// #include <bits/stdc++.h> 
// int mod=(1e9+7);
// int findWaysUtil(int ind, int target, vector<int>& arr, vector<vector<int>> &dp){

//     if(ind == 0){
//             if(target==0 && arr[0]==0)
//                 return 2;
//             if(target==0 || target == arr[0])
//                 return 1;
//             return 0;
//     }
    
//     if(dp[ind][target]!=-1)
//         return dp[ind][target];
        
//     int notTaken = findWaysUtil(ind-1,target,arr,dp);
    
//     int taken = 0;
//     if(arr[ind]<=target)
//         taken = findWaysUtil(ind-1,target-arr[ind],arr,dp);
        
//     return dp[ind][target]= (notTaken + taken)%mod;
// }
// int countPartitions(int n, int d, vector<int> &arr) {
//     int total_sum=0;
//     for(int x:arr) total_sum+=x;
//     vector<vector<int>> dp(n,vector<int>(total_sum+1,-1));
//     if(total_sum-d<0||(total_sum-d)%2) return false;
//     return findWaysUtil(n-1,(total_sum-d)/2,arr,dp);
// }
