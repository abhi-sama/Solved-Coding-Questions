class Solution {
public:
    bool subsetSumToK(int n, int k, vector<int> &arr) {
        vector<bool> prev(k+1,false);
        vector<bool> cur(k+1,false);
        prev[0]=cur[0]=true;
        if (arr[0] <= k)
            prev[arr[0]] = true;
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
    bool canPartition(vector<int>& nums) {
     int total_sum=0;
        for(int x:nums)
            total_sum+=x;
        if(total_sum%2) return false;
        int target=total_sum/2;
        return subsetSumToK(nums.size(),target,nums);
    }
};