class Solution
{
	public:
	
	    // Function to find all LCS
        void findAllLCS(vector<vector<int>>& dp, const string& s1, const string& s2,
                                int i, int j, string& current, set<string>& lcsSet) {
            if (i == 0 || j == 0) {
                lcsSet.insert(current);
                return;
            }
        
            if (s1[i-1] == s2[j-1]) {
                current = s1[i-1] + current;
                findAllLCS(dp, s1, s2, i-1, j-1, current, lcsSet);
                current.erase(current.begin());
            } else {
                if (dp[i-1][j] >= dp[i][j-1]) {
                    findAllLCS(dp, s1, s2, i-1, j, current, lcsSet);
                }
                if (dp[i][j-1] >= dp[i-1][j]) {
                    findAllLCS(dp, s1, s2, i, j-1, current, lcsSet);
                }
            }
        }
        
		vector<string> all_longest_common_subsequences(string s1, string s2)
		{
		    
          int n = s1.size();
          int m = s2.size();
        
          vector < vector < int >> dp(n + 1, vector < int > (m + 1, 0));
          for (int i = 0; i <= n; i++) {
            dp[i][0] = 0;
          }
          for (int i = 0; i <= m; i++) {
            dp[0][i] = 0;
          }
        
          for (int ind1 = 1; ind1 <= n; ind1++) {
            for (int ind2 = 1; ind2 <= m; ind2++) {
              if (s1[ind1 - 1] == s2[ind2 - 1])
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1];
              else
                dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1]);
            }
          }
          
            set<string> lcsSet;
            string current = "";
            findAllLCS(dp, s1, s2, n, m, current, lcsSet);
            vector<string> res;
            for(auto s:lcsSet)
                res.push_back(s);
            return res;
            
		}
};