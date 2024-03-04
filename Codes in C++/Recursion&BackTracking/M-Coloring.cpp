bool isValid(int node,vector<vector<int>> &mat,vector<int> &color,int col)
{
	for (int i = 0; i < mat.size(); i++)
	{
		if (i!=node && mat[node][i] && color[i] == col)
		{
			return false;
		}
	}

	return true;
}

bool solve(int node,vector<vector<int>> &mat, vector<int> &color ,int n,int m)
{
    if(node==n)
        return true;

    for(int i=1;i<=m;i++)
    {
        if(isValid(node,mat,color,i))
        {
            color[node]=i;
            if(solve(node+1,mat,color,n,m))
            return true;
            color[node]=0;
        }
    }

    return false;
}

string graphColoring(vector<vector<int>> &mat, int m) {
    int n=mat.size();
    vector<int> color(n,0);
    if(solve(0,mat,color,n,m)) return "YES";
    return "NO";
}