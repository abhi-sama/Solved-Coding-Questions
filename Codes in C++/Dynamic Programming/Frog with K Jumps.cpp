int minimizeCost(int n, int k, vector<int> &height){
    vector<int> dp(n,0);
    dp[0]=0;
    for(int i=1;i<n;i++)
    {   int minE=INT_MAX;
        for(int j=1;j<=k;j++)
        {
            if(i-j>=0)
            {
                minE=min(minE,dp[i-j]+abs(height[i]-height[i-j]));
            }
        }
        dp[i]=minE;
    }
    return dp[n-1];
}