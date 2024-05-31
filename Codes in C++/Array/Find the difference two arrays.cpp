class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> res;
        unordered_set<int> A, B;

        for (auto it : nums1)
            A.insert(it);
        for (auto it : nums2)
            B.insert(it);
        vector<int> X, Y;
        for (auto i : A) {
            if (B.find(i) == B.end()) {
                X.push_back(i);
            }
        }
        for (auto i : B) {
            if (A.find(i) == A.end()) {
                Y.push_back(i);
            }
        }

        vector<vector<int>> ans;
        ans.push_back(X);
        ans.push_back(Y);

        return ans;
    }
};