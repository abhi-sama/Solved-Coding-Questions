class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int prefix_sum=0;
        int total_sum=accumulate(nums.begin(),nums.end(),0);
        int suffix_sum=total_sum;
        for(int i=0;i<nums.size();i++)
        {   if(i!=0)
                prefix_sum+=nums[i-1];
            suffix_sum=(total_sum-prefix_sum-nums[i]);

            if(prefix_sum==suffix_sum)
                 return i;
        }
        return -1;
    }
};