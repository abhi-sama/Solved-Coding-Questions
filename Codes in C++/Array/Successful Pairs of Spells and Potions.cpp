class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions,
                                long long success) {
        int m = spells.size();
        int n = potions.size();
        sort(potions.begin(), potions.end());
        vector<int> res;
        for (int i = 0; i < m; i++) {
            int left = 0;
            int right = n - 1;
            long long spell = spells[i];
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (spell * potions[mid] >= success) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            res.push_back(n - left);
        }
        return res;
    }
};