class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
      int m=triangle.size();
      int n=triangle[m-1].size();
      vector<int> front(n,0),cur(n,0);
      front=triangle[m-1];
      for(int i=n-2;i>=0;i--)
      {
          for(int j=i;j>=0;j--)
          {
              int down=triangle[i][j]+front[j];
              int diag=triangle[i][j]+front[j+1];
              cur[j]=min(down,diag); 
          }
          front=cur;
      }
    return front[0];
    }
};