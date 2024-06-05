class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int maxLen = 0, l = 0, zeroes = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] == 0)
                zeroes++;
            if (zeroes > 1) {
                if (nums[l] == 0)
                    zeroes--;
                l++;
            }
            if (zeroes <= 1) {
                maxLen = max(maxLen, r - l + 1);
            }
        }
        return maxLen - 1;
    }
};