class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m=text1.size();
        int n=text2.size();
        vector<int> prev(n+1,0);
        //Intialise
        for(int i=0;i<=n;i++) prev[i]=0;

        for(int i=1;i<=m;i++)
        {   vector<int> cur(n+1,0);
            for(int j=1;j<=n;j++)
            {
                if(text1[i-1]==text2[j-1]) 
                    cur[j]=1+prev[j-1];
                else
                    cur[j]=max(prev[j],cur[j-1]);
            }
            prev=cur;
        }
        return prev[n];
    }
};



// Print one LCS
        //  int len = dp[n][m];
        //   int i = n;
        //   int j = m;
        
        //   int index = len - 1;
        //   string str = "";
        //   for (int k = 1; k <= len; k++) {
        //     str += "$"; // dummy string
        //   }
        
        //   while (i > 0 && j > 0) {
        //     if (s1[i - 1] == s2[j - 1]) {
        //       str[index] = s1[i - 1];
        //       index--;
        //       i--;
        //       j--;
        //     } else if (s1[i - 1] > s2[j - 1]) {
        //       i--;
        //     } else j--;
        //   }
		// }




// class Solution
// {
// public:
//     int longestCommonSubsequence(string text1, string text2)
//     {
//         int m = text1.length();
//         int n = text2.length();
//         int LCS[m + 1][n + 1];
//         for (int i = 0; i < m + 1; i++)
//         {
//             for (int j = 0; j < n + 1; j++)
//             {
//                 LCS[i][j] = 0;
//             }
//         }
//         for (int i = 1; i <= m; i++)
//             for (int j = 1; j <= n; j++)
//             {
//                 if (text1[i - 1] == text2[j - 1])
//                     LCS[i][j] = LCS[i - 1][j - 1] + 1;
//                 else
//                     LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1]);
//             }
//         return LCS[m][n];
//     }
// };