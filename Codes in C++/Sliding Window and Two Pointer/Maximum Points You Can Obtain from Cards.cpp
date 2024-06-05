class Solution {
public:
    int maxScore(vector<int>& nums, int k) {
        int lSum = 0, rSum = 0, maxSum = 0;
        for (int i = 0; i < k; i++)
            lSum += nums[i];
        maxSum = lSum;
        int rIndex = nums.size() - 1;
        for (int i = k - 1; i >= 0; i--) {
            lSum = lSum - nums[i];
            rSum = rSum + nums[rIndex];
            rIndex--;
            maxSum = max(maxSum, lSum + rSum);
        }
        return maxSum;
    }
};