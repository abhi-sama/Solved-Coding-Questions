class Solution {
public:
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
            
                dp[ind][target]= (notTaken + taken);
            }
        }
        return dp[n-1][tar];
    }

    int findTargetSumWays(vector<int>& nums, int target) {
        int total_sum=0;
        for(int x:nums) total_sum+=x;
        if(total_sum-target<0||(total_sum-target)%2) return false;
        return findWays(nums,(total_sum-target)/2); 
    }
};