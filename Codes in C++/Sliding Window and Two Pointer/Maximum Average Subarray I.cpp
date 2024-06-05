class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double maxAvg = 0;
        double sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        maxAvg = sum / k;
        int l = 0, r = k;
        while (r < nums.size()) {
            sum = sum - nums[l++] + nums[r++];
            maxAvg = max(maxAvg, (sum / k));
        }
        return maxAvg;
    }
};