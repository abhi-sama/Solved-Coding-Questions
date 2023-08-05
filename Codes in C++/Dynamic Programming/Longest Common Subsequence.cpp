class Solution
{
public:
    int longestCommonSubsequence(string text1, string text2)
    {
        int m = text1.length();
        int n = text2.length();
        int LCS[m + 1][n + 1];
        for (int i = 0; i < m + 1; i++)
        {
            for (int j = 0; j < n + 1; j++)
            {
                LCS[i][j] = 0;
            }
        }
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
            {
                if (text1[i - 1] == text2[j - 1])
                    LCS[i][j] = LCS[i - 1][j - 1] + 1;
                else
                    LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1]);
            }
        return LCS[m][n];
    }
};