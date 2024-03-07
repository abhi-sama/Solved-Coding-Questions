class Solution {
public:
    long long int helper(vector<int>& nums) {
    int prev2=0;
    int prev=nums[0];
    int curi=-1;
    int n=nums.size();
    for(int i=1;i<n;i++)
    {
        int pick = nums[i];
        if(i>1)
            pick+=prev2;
        int not_pick = 0 + prev;
        curi=max(pick,not_pick);
        prev2=prev;
        prev=curi;
    }
    return prev;
    }
    long long int rob(vector<int>& nums) {
     int n=nums.size();
     vector<int> temp1,temp2;
     if(n==1) return nums[0];
     for(int i=0;i<n;i++)
     {
         if(i!=0)
            temp2.push_back(nums[i]);
         if(i!=(n-1))
            temp1.push_back(nums[i]);
     }
     return max(helper(temp1),helper(temp2));
    }
};