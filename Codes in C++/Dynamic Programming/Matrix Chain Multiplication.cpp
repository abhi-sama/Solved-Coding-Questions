class Solution
{
public:
    int matrixMultiplication(int N, int arr[])
    {
        vector<vector<int>> mcm(N, vector<int>(N, 0));
        for (int i = N - 1; i >= 1; i--)
        {
            for (int j = i + 1; j < N; j++)
            {

                mcm[i][j] = INT_MAX;
                for (int k = i; k < j; k++)
                {
                    mcm[i][j] = min(mcm[i][j], mcm[i][k] 
                                    + mcm[k + 1][j] 
                                    + arr[i - 1] * arr[k] * arr[j]);
                }
            }
        }
        return mcm[1][N - 1];
    }
};