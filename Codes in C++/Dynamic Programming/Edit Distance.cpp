class Solution {
public:
    int minDistance(string word1, string word2) {
    int ED[word1.length()+1][word2.length()+1];
    for (int i = 0; i <= word1.length(); i++)
 	    for (int j = 0; j <= word2.length(); j++)
        {
            if(i==0)ED[i][j]=j;
            else if(j==0)ED[i][j]=i;
            else if(word1[i-1]==word2[j-1])ED[i][j]=ED[i-1][j-1];
            else ED[i][j]=min(min(ED[i-1][j],ED[i][j-1]),ED[i-1][j-1])+1;
        }
        return ED[word1.length()][word2.length()];
    }
};