class Solution {
public:
    void dfs(int index, int sum, int k, vector<int>& list,
             vector<vector<int>>& ans) {
        if (list.size() == k && sum == 0) {
            ans.push_back(list);
            return;
        }
        for (int i = index; i <= 9; i++) {
            list.push_back(i);
            dfs(i + 1, sum - i, k, list, ans);
            list.pop_back();
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ans;
        vector<int> list;
        dfs(1, n, k, list, ans);
        return ans;
    }
    // TC - > O(9 ^k).
    // SC-> O(k)
};