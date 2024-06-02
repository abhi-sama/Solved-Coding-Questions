class Solution {
public:
    bool closeStrings(string word1, string word2) {
        int m = word1.length();
        int n = word2.length();
        if (m != n)
            return false;
        vector<int> freq1(26, 0);
        vector<int> freq2(26, 0);
        for (int i = 0; i < m; i++) {
            char ch1 = word1[i];
            char ch2 = word2[i];
            freq1[ch1 - 'a']++;
            freq2[ch2 - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (!freq1[i] == 0 && !freq2[i] == 0)
                continue;
            if (freq1[i] == 0 && freq2[i] == 0)
                continue;
            return false;
        }
        sort(freq1.begin(), freq1.end());
        sort(freq2.begin(), freq2.end());
        return freq1 == freq2;
    }
};