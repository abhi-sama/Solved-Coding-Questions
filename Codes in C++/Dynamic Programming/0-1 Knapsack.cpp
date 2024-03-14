int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight) 
{
	vector<int> prev(maxWeight+1,0);
	for(int i=weight[0];i<=maxWeight;i++)prev[i]=value[0];
	for(int ind=1;ind<n;ind++)
	{
		for(int W=maxWeight;W>=0;W--)
		{
		int not_pick=0 + prev[W];
		int pick=INT_MIN;
		if(weight[ind]<=W)
			pick=value[ind]+prev[W-weight[ind]];
		prev[W]=max(pick,not_pick);
		}
	}
	
	return prev[maxWeight];
}


// int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight) 
// {
// 	vector<int> prev(maxWeight+1,0);
// 	vector<int> cur(maxWeight+1,0);
// 	for(int i=weight[0];i<=maxWeight;i++)prev[i]=value[0];
// 	for(int ind=1;ind<n;ind++)
// 	{
// 		for(int W=0;W<=maxWeight;W++)
// 		{
// 		int not_pick=0 + prev[W];
// 		int pick=INT_MIN;
// 		if(weight[ind]<=W)
// 			pick=value[ind]+prev[W-weight[ind]];
// 		cur[W]=max(pick,not_pick);
// 		}
// 		prev=cur;
// 	}
	
// 	return prev[maxWeight];
// }



// int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight) 
// {
// 	vector<vector<int>> dp(n,vector<int>(maxWeight+1,0));
// 	for(int i=weight[0];i<=maxWeight;i++)dp[0][i]=value[0];
// 	for(int ind=1;ind<n;ind++)
// 	{
// 		for(int W=0;W<=maxWeight;W++)
// 		{
// 		int not_pick=0 + dp[ind-1][W];
// 		int pick=INT_MIN;
// 		if(weight[ind]<=W)
// 			pick=value[ind]+dp[ind-1][W-weight[ind]];
// 		dp[ind][W]=max(pick,not_pick);
// 		}
// 	}
	
// 	return dp[n-1][maxWeight];
// }







// #include <bits/stdc++.h>
// int f(int ind,int maxWeight,vector<int> &weight,
//  vector<int> &value,vector<vector<int>> &dp)
// {
// 	if(ind==0)
// 	{
// 		if(weight[0]<=maxWeight)
// 			 return value[0];
// 		else 
// 			return 0;
// 	}

// 	if(dp[ind][maxWeight]!=-1) 
// 		return dp[ind][maxWeight];

// 	int not_pick=0 + f(ind-1,maxWeight,weight,value,dp);
// 	int pick=INT_MIN;
// 	if(weight[ind]<=maxWeight)
// 		pick=value[ind]+f(ind-1,maxWeight-weight[ind],weight,value,dp);
// 	dp[ind][maxWeight]=max(pick,not_pick);
// 	return dp[ind][maxWeight];
// }
// int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight) 
// {
// 	vector<vector<int>> dp(n,vector<int>(maxWeight+1,-1));
	
// 	return f(n-1,maxWeight,weight,value,dp);
// }





// int maxProfit(vector<int> &values, vector<int> &weights, int n, int w)
// {
// 	int ks[n+1][w+1];
//     for (int i = 0; i < n + 1; i++)
// 		ks[i][0] = 0;
//  	for (int j = 0; j < w + 1; j++)
//         ks[0][j] = 0;

// 	for(int i=1;i<=n;i++)
// 	{
// 		for(int j=1;j<=w;j++)
// 		{
// 			int dont=ks[i-1][j];
// 			ks[i][j]=dont;
// 			if(j-weights[i-1]>=0)
// 			{
// 			int take=ks[i-1][j-weights[i-1]]+values[i-1];
// 			ks[i][j]=max(take,dont);

// 			}	 			
// 		}
// 	}
// 	return ks[n][w];
// }
