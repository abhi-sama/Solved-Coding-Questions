class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    int startIndex=0;
    int endIndex=0;
    long long maxSum=-1;
    long long currSum=0;
    //Modified Kadane if there is no postive value
    int maxele=*max_element(nums.begin(),nums.end());
    if(maxele<=0)return maxele;

    for(int i=0;i<nums.size();i++)
    {
      if (currSum + nums[i] >= 0) {
        currSum += nums[i];
      }
      else {
          startIndex=i;
          currSum=0;
      }
        if(currSum>maxSum)
        maxSum=currSum;
    }
    return maxSum;
    }
};