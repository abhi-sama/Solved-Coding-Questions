
#include <bits/stdc++.h> 
int maximumChocolates(int r, int c, vector<vector<int>> &grid) {
     vector<vector<int>> front(c, vector<int>(c, 0));
     vector<vector<int>> cur(c, vector<int>(c, 0));
       for (int j1 = 0; j1 < c; j1++) {
        for (int j2 = 0; j2 < c; j2++) {
            if (j1 == j2)
                front[j1][j2] = grid[r - 1][j1];
            else
                front[j1][j2] = grid[r - 1][j1] + grid[r - 1][j2];
        }}
        for (int i = r - 2; i >= 0; i--) {
            for (int j1 = 0; j1 < c; j1++) {
                for (int j2 = 0; j2 < c; j2++) {
                    int maxi = INT_MIN;
                    for (int di = -1; di <= 1; di++) {
                        for (int dj = -1; dj <= 1; dj++) {
                            int ans;

                            if (j1 == j2)
                                ans = grid[i][j1];
                            else
                                ans = grid[i][j1] + grid[i][j2];

                            if ((j1 + di < 0 || j1 + di >= c) || (j2 + dj < 0 || j2 + dj >= c))
                                ans += INT_MIN; 
                            else
                                ans += front[j1 + di][j2 + dj]; 

                            maxi = max(ans, maxi); 
                        }
                    }
                    cur[j1][j2] = maxi; 
                }
            }
            front=cur;
        } 
        
    
    
    return front[0][c - 1];
}
// #include <bits/stdc++.h> 
// int maximumChocolates(int r, int c, vector<vector<int>> &grid) {
//    vector<vector<vector<int>>> dp(r, vector<vector<int>>(c, vector<int>(c, 0)));
//        for (int j1 = 0; j1 < c; j1++) {
//         for (int j2 = 0; j2 < c; j2++) {
//             if (j1 == j2)
//                 dp[r - 1][j1][j2] = grid[r - 1][j1];
//             else
//                 dp[r - 1][j1][j2] = grid[r - 1][j1] + grid[r - 1][j2];
//         }}
//         for (int i = r - 2; i >= 0; i--) {
//             for (int j1 = 0; j1 < c; j1++) {
//                 for (int j2 = 0; j2 < c; j2++) {
//                     int maxi = INT_MIN;
//                     for (int di = -1; di <= 1; di++) {
//                         for (int dj = -1; dj <= 1; dj++) {
//                             int ans;

//                             if (j1 == j2)
//                                 ans = grid[i][j1];
//                             else
//                                 ans = grid[i][j1] + grid[i][j2];

//                             if ((j1 + di < 0 || j1 + di >= c) || (j2 + dj < 0 || j2 + dj >= c))
//                                 ans += INT_MIN; 
//                             else
//                                 ans += dp[i + 1][j1 + di][j2 + dj]; 

//                             maxi = max(ans, maxi); 
//                         }
//                     }
//                     dp[i][j1][j2] = maxi; 
//                 }
//             }
//         } 
        
    
    
//     return dp[0][0][c - 1];
// }