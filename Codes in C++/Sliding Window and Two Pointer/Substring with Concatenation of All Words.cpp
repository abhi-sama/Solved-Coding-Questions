class Solution {
    unordered_map<string, int> mpp;

public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        int length = words[0].size();
        mpp.clear();
        for (auto x : words)
            mpp[x]++;
        for (int offset = 0; offset < length; offset++) {
            int size = 0;
            unordered_map<string, int> seen;
            for (int i = offset; i + length <= s.size(); i += length) {

                string sub = s.substr(i, length);
                auto itr = mpp.find(sub);
                if (itr == mpp.end()) {
                    seen.clear();
                    size = 0;
                    continue;
                }
                ++seen[sub];
                ++size;
                while (seen[sub] > itr->second) {
                    string first = s.substr(i - (size - 1) * length, length);
                    --seen[first];
                    --size;
                }
                if (size == words.size()) {
                    res.push_back(i - (size - 1) * length);
                }
            }
        }
        return res;
    }
};