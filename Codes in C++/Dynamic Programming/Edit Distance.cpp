class Solution {
public:
    int minDistance(string word1, string word2) {
    int m=word1.length();
    int n=word2.length();
    vector<int> prev(n+1),cur(n+1);
    for(int i=0;i<=n;i++) prev[i]=i;
    for (int i = 1; i <= m; i++)
    {   cur[0]=i;
 	    for (int j = 1; j <= n; j++)
        {
            if(word1[i-1]==word2[j-1])cur[j]=prev[j-1];
            else cur[j]=min(min(prev[j],cur[j-1]),prev[j-1])+1;
        }
        prev=cur;
    }
        return prev[n];
    }
};
// class Solution {
// public:
//     int minDistance(string word1, string word2) {
//     int ED[word1.length()+1][word2.length()+1];
//     for (int i = 0; i <= word1.length(); i++)
//  	    for (int j = 0; j <= word2.length(); j++)
//         {
//             if(i==0)ED[i][j]=j;
//             else if(j==0)ED[i][j]=i;
//             else if(word1[i-1]==word2[j-1])ED[i][j]=ED[i-1][j-1];
//             else ED[i][j]=min(min(ED[i-1][j],ED[i][j-1]),ED[i-1][j-1])+1;
//         }
//         return ED[word1.length()][word2.length()];
//     }
// };