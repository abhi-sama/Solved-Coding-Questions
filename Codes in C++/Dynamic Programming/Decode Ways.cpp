    int numDecodings(string s) {
        int n = s.size();
        vector<int> dp(n + 1, 0);
        dp[n] = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '0') {
                dp[i] = 0;
                continue;
            }
            int res = dp[i + 1];
            if (i + 1 < s.length() &&
                (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6')))
                res += dp[i + 2];
            dp[i] = res;
        }
        return dp[0];
    }

// class Solution {
// public:
//     int helper(int i,string s,vector<int> &dp){
//         if(i==s.length())
//             return 1;
//         if(dp[i]!=-1) return dp[i];
//         if(s[i]=='0')
//             return 0;
//         int res=helper(i+1,s,dp);
//         if(i+1<s.length()&&(s[i]=='1'||(s[i]=='2'&&s[i+1]<='6')))
//             res+=helper(i+2,s,dp);
//         return dp[i]=res;
//     }
//     int numDecodings(string s) {
//         vector<int> dp(s.length(),-1);
//         return helper(0,s,dp);
//     }
// };