class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    long long maxSum=-1;
    long long currSum=0;
    //Modified Kadane if there is no postive value
    int maxele=*max_element(nums.begin(),nums.end());
    if(maxele<=0)return maxele;
    int start=-1;
    int ansStart=-1;
    int ansEnd=-1;
    for(int i=0;i<nums.size();i++)
    { if (currSum==0)start=i;
      if (currSum + nums[i] >= 0) {
        currSum += nums[i];
        ansStart=start;
        ansEnd=i;
      }
      else {
          currSum=0;
      }
        if(currSum>maxSum)
        maxSum=currSum;
    }
    return maxSum;
    }
};