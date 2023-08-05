int maxProfit(vector<int> &values, vector<int> &weights, int n, int w)
{
	int ks[n+1][w+1];
    for (int i = 0; i < n + 1; i++)
		ks[i][0] = 0;
 	for (int j = 0; j < w + 1; j++)
        ks[0][j] = 0;

	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=w;j++)
		{
			int dont=ks[i-1][j];
			ks[i][j]=dont;
			if(j-weights[i-1]>=0)
			{
			int take=ks[i-1][j-weights[i-1]]+values[i-1];
			ks[i][j]=max(take,dont);

			}	 			
		}
	}
	return ks[n][w];
}
