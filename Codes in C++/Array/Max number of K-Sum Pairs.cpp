class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> mpp;
        int count = 0;
        for (auto i : nums) {
            if (mpp[k - i] > 0) {
                mpp[k - i]--;
                count++;
            } else {
                mpp[i]++;
            }
        }
        return count;
    }
};