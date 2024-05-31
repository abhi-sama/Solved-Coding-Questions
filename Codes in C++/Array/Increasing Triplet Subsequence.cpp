class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first_min = INT_MAX;
        int second_min = INT_MAX;
        for (int n : nums) {
            if (n <= first_min)
                first_min = n;
            else if (n <= second_min)
                second_min = n;
            else
                return true;
        }

        return false;
    }
};