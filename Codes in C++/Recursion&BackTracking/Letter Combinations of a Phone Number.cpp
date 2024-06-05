class Solution {
public:
    string dgmp[10] = {"",    "",    "abc",  "def", "ghi",
                       "jkl", "mno", "pqrs", "tuv", "wxyz"};
    void dfs(string digits, int index, string combo, vector<string>& res) {
        if (index == digits.length()) {
            res.push_back(combo);
            return;
        }
        string letters = dgmp[digits[index] - '0'];
        for (auto ch : letters) {
            dfs(digits, index + 1, combo + ch, res);
        }
    }
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits.empty())
            return res;
        dfs(digits, 0, "", res);
        return res;
    }
};