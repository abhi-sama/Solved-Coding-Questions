class Solution {
public:
    int rob(vector<int>& nums) {
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
};