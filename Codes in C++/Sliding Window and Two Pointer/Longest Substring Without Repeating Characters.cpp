class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, r = 0, maxLen = 0;
        vector<int> hash(256, -1);
        int n = s.length();
        while (r < n) {
            if (hash[s[r]] >= l)
                l = hash[s[r]] + 1;
            maxLen = max(maxLen, (r - l + 1));
            hash[s[r]] = r;
            r++;
        }
        return maxLen;
    }
};