class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> prev(n,0);
        for(int i=0;i<m;i++)
        {   vector<int> temp(n,0);
            for(int j=0;j<n;j++)
            {   
                if(i==0&&j==0) 
                    temp[0]=1;
                if(i>0)
                    temp[j]+=prev[j];
                if(j>0)
                    temp[j]+=temp[j-1];
            }
            prev=temp;
        }
    return prev[n-1];    
    }

};
///////SuperOptimalSolution
// class Solution {
// public:
//     long int uniquePaths(int m, int n) {
//        long int N=m+n-2;
//        long int r=m-1;
//         long int res=1;
//         for(long int i=1;i<=r;i++)
//         {   
//             res=res*(N-r+i)/i;
//         }
//     return (int)res; 
//     }
// };
// class Solution {
// public:
//     int uniquePaths(int m, int n) {
//         vector<vector<int>> dp(m,vector<int>(n,0));
//         for(int i=0;i<m;i++)
//         {
//             for(int j=0;j<n;j++)
//             {
//                 if(i==0&&j==0) 
//                     dp[0][0]=1;
//                 if(i>0)
//                     dp[i][j]+=dp[i-1][j];
//                 if(j>0)
//                     dp[i][j]+=dp[i][j-1];
//             }
//         }
//     return dp[m-1][n-1];    
//     }
// };
