#define m 1000000007
class Solution
{
public:
    int countFriendsPairings(int n) 
    { 
        if (n <= 2) { 
    		return n; 
    	} 
        long long cur=0, prev1=2,prev2=1;
        for(int i=3;i<=n;i++){

                cur=(prev1%m+(i-1)*(prev2)%m)%m;
                prev2=prev1;
                prev1=cur;
            
        }
        return cur%m;
    }
};    

// #define m 1000000007
// class Solution
// {
// public:
//     int countFriendsPairings(int n) 
//     { 
//         vector<long long> dp(n+1,0);
//         for(int i=0;i<=n;i++){
//             if(i<=2)
//                 dp[i]=i;
//             else {
//                 dp[i]=(dp[i-1]%m+(i-1)*(dp[i-2])%m)%m;
//             }
//         }
//         return dp[n]%m;
//     }
// };    