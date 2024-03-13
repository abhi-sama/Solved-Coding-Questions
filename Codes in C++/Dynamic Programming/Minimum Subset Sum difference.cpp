int minSubsetSumDifference(vector<int>& nums, int n)
{
        int total_sum=0;
        for(auto x:nums)total_sum+=x;
        int k=total_sum;
        vector<bool> prev(k+1,false);
        vector<bool> cur(k+1,false);
        prev[0]=cur[0]=true;
        prev[nums[0]]=true;
        for(int i=1;i<nums.size();i++)
        {
            for(int target=0;target<=k;target++)
            {
                bool not_take=prev[target];
                bool take=false;
                if(nums[i]<=target)
                    take=prev[target-nums[i]];
                cur[target]=not_take||take;
            }
            prev=cur;
        }
        int mini=1e7;
        for( int i=0;i<=k;i++)
        {
            int s1=i;
            int s2=total_sum-i;
            if(prev[i])
                mini=min(mini,abs(s1-s2));
        }
        return mini;
}
