class Solution {
public:
    bool isSubsequence(string s, string t) {
        int ps = 0;
        int pt = 0;
        int m = s.length();
        int n = t.length();
        while (ps < m && pt < n) {
            if (s[ps] == t[pt])
                ps++;
            pt++;
        }
        if (ps == m)
            return true;
        return false;
    }
};