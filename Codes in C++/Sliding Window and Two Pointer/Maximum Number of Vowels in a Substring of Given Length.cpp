class Solution {
public:
    bool isVowel(char a) {
        return a == 'u' || a == 'e' || a == 'o' || a == 'a' || a == 'i';
    }
    int maxVowels(string s, int k) {
        int maxCount = 0, count = 0;
        for (int i = 0; i < k; i++)
            if (isVowel(s[i]))
                count++;
        maxCount = count;
        int n = s.length();
        for (int r = k; r < n; r++) {
            if (isVowel(s[r]))
                count++;
            if (isVowel(s[r - k]))
                count--;
            maxCount = max(maxCount, count);
        }
        return maxCount;
    }
};