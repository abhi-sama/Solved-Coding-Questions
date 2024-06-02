class Solution {
public:
    vector<int> asteroidCollision(vector<int>& ast) {
        int n = ast.size();
        vector<int> ans;
        for (auto a : ast) {
            while (!ans.empty() && a < 0 && ans.back() > 0) {
                int sum = a + ans.back();
                if (sum < 0) {
                    ans.pop_back();
                } else if (sum > 0) {
                    a = 0;
                } else if (sum == 0) {
                    ans.pop_back();
                    a = 0;
                }
            }
            if (a != 0)
                ans.push_back(a);
        }
        return ans;
    }
};