class Solution {
public:
    static bool vowel(char c) {
        c = tolower(c);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            return true;
        return false;
    }
    string reverseVowels(string s) {
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            if (vowel(s[i]) && vowel(s[j])) {
                swap(s[i], s[j]);
                i++;
                j--;
            } else if (vowel(s[i]) && !vowel(s[j])) {
                j--;
            } else if (!vowel(s[i]) && vowel(s[j])) {
                i++;
            } else {
                i++;
                j--;
            }
        }
        return s;
    }
};