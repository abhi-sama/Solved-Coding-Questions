class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int maxLen = 0, l = 0, zeroes = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] == 0)
                zeroes++;
            if (zeroes > k) {
                if (nums[l] == 0)
                    zeroes--;
                l++;
            }
            if (zeroes <= k) {
                maxLen = max(maxLen, r - l + 1);
            }
        }
        return maxLen;
    }
};