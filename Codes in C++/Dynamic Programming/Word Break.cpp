class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n=s.size();
    vector<bool>  dp(n+1,false);
      dp[n]=true;
      for(int i=n-1;i>=0;i-- ){
        for( auto& w:wordDict){
            if((i+w.size())<=n && s.substr(i,w.size())==w)
                dp[i]=dp[i+w.size()];
            if(dp[i])break;
        }
      }
      return dp[0];
    }
};


    // bool wordBreak(string s, vector<string>& wordDict) {
    // vector<bool> dp(s.length(),false); 
    // for(int i=0;i<s.length();i++)
    // {
    //     for(string word:wordDict)
    //     {
    //         int currSize=word.size();
    //         // Handle out of bounds case
    //         if(i-currSize+1<0)
    //             continue;
    //         if(i==word.length()-1||dp[i-word.length()])
    //             if(s.substr(i-currSize+1,currSize)==word)
    //             {
    //                 dp[i]=true;
    //                 break;
    //             }
    //     }  
    // }
    // return dp[s.length() - 1];
    // }
// **************************Top-Down Approach********************************
// class Solution {
// public:
//     vector<int> memo;
//     vector<string> wordDict;
//     string s;
//     bool dp(int i)
//     {
//         if(i<0)
//             return true;
//         if(memo[i]!=-1)
//             return memo[i]==1;
//         for(string word:wordDict)
//         {
//             int currSize=word.size();
//             // Handle out of bounds case
//             if(i-currSize+1<0)
//                 continue;
//             if(s.substr(i-currSize+1,currSize)==word && dp(i-currSize))
//             {
//                 memo[i]=1;
//                 return true;
//             }
//         }
//         memo[i]=0;
//         return false;
//     }
//     bool wordBreak(string s, vector<string>& wordDict) {
//         memo = vector(s.length(), -1);
//         this->wordDict = wordDict;
//         this->s = s;
//         return dp(s.length() - 1);  
//     }
// };
// **************************Approach-1********************************
// class Solution {
// public:
//     bool wordBreak(string s, vector<string>& wordDict) {
//         map<string,bool> dic;
//         bool WB[s.length()][s.length()];
//         for(string s:wordDict)
//             dic[s]=true;

//         int j=0;
//         for(int len=1;len<=s.length();len++)
//         for(int i=0;i<=s.length()-len;i++)
//         {
//             j=i+len-1;
//             WB[i][j]=false;
//         }

//         j=0;
//         for(int len=1;len<=s.length();len++)
//         for(int i=0;i<=s.length()-len;i++)
//         {
//             j=i+len-1;
//             if(dic[s.substr(i,j-i+1)]==true)
//                 WB[i][j]=true;
//             else 
//             {
                
//                 for(int k=i;k<j;k++)
//                 {
//                     if(WB[i][k]&&WB[k+1][j])
//                         {WB[i][j]=true;
//                         break;}
//                 }
//             }

//         }

//         j=0;
//         for(int len=1;len<=s.length();len++)
//         for(int i=0;i<=s.length()-len;i++)
//         {
//             j=i+len-1;
//            cout<< WB[i][j]<<"\n"<<"("<<i<<j<<")"<<endl;
//         }

//             return WB[0][s.length()-1];
//     }
// };