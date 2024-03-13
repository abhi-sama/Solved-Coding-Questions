int findWays(vector<int>& arr, int k)
{	int n=arr.size();
    vector<int> prev(k+1,0);
    vector<int> cur(k+1,0);
    prev[0]=cur[0]=1;
    if(arr[0]<=k)
        prev[arr[0]]=1;
    for(int i=1;i<n;i++)
    {
        for(int target=0;target<=k;target++)
        {
            int not_take=prev[target];
            int take=0;
            if(arr[i]<=target)
                take=prev[target-arr[i]];
            cur[target]=not_take+take;
        }
        prev=cur;
    }
    return prev[k];
}
