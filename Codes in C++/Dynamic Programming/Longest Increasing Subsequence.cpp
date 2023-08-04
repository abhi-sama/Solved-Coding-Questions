class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
    int n=nums.size();
    vector<int> len(n,1);
    for(int i=1;i<n;i++)
    {
     for(int j=i-1;j>=0;j--)
     { 
         if(nums[i]>nums[j])
         len[i]=max(len[j]+1,len[i]);
     }
    } 
    return *max_element(len.begin(),len.end());
    }
};