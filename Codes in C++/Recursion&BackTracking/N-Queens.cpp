 //Optimise N-Queens
 class Solution {
    void solve(int col,int n,vector<string> &board,vector<vector<string>> &ans,
    vector<int> &leftRow,vector<int> &upperDiag,vector<int> &lowerDiag)
    {
        if(col==n)
        {
        ans.push_back(board);
        return;
        } 

        for(int row=0;row<n;row++)
        {
            if(leftRow[row]==0&&upperDiag[n-1 +col-row]==0&&lowerDiag[row+col]==0)
            {   leftRow[row]=1;
                upperDiag[n-1 +col-row]=1;
                lowerDiag[row+col]=1;
                board[row][col]='Q';
                solve(col+1,n,board,ans,leftRow,upperDiag,lowerDiag);
                board[row][col]='.';
                leftRow[row]=0;
                upperDiag[n-1 + col-row]=0;
                lowerDiag[row+col]=0;
            }
        }
        return;
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n);
        vector<vector<string>> ans;
        string s(n,'.');
        for(int i=0;i<n;i++)
        {
            board[i]=s;
        }
        vector<int> leftRow(n,0),upperDiag(2*n-1,0),lowerDiag(2*n-1,0);
        solve(0,n,board,ans,leftRow,upperDiag,lowerDiag);
        return ans;
    }
};
//when return type is vector<vector<int>>
/*
    void solve(int col,int n,vector<vector<int>> &board,
    vector<vector<int>> &ans,
    vector<int> &leftRow,vector<int> &upperDiag,vector<int> &lowerDiag)
    {
        if(col==n)
        {
        vector<int> temp;

        for(auto it:board)

        {

            for(int i=0;i<it.size();i++)

              temp.push_back(it[i]);

        }  

        ans.push_back(temp);
        } 

        for(int row=0;row<n;row++)
        {
            if(leftRow[row]==0&&upperDiag[n-1 +col-row]==0&&lowerDiag[row+col]==0)
            {   leftRow[row]=1;
                upperDiag[n-1 +col-row]=1;
                lowerDiag[row+col]=1;
                board[row][col]=1;
                solve(col+1,n,board,ans,leftRow,upperDiag,lowerDiag);
                board[row][col]=0;
                leftRow[row]=0;
                upperDiag[n-1 + col-row]=0;
                lowerDiag[row+col]=0;
            }
        }
        return;
    }

vector<vector<int>> solveNQueens(int n) {
        vector<vector<int>> board(n,vector<int>(n,0));
        vector<vector<int>> ans;
        /*string s(n,'.');
        for(int i=0;i<n;i++)
        {
            board[i]=s;
        }
        vector<int> leftRow(n,0),upperDiag(2*n-1,0),lowerDiag(2*n-1,0);
        solve(0,n,board,ans,leftRow,upperDiag,lowerDiag);
        return ans;
}
*/
 
 /*bool isSafe1(int row, int col, vector < string > board, int n) {
      // check upper element
      int duprow = row;
      int dupcol = col;

      while (row >= 0 && col >= 0) {
        if (board[row][col] == 'Q')
          return false;
        row--;
        col--;
      }

      col = dupcol;
      row = duprow;
      while (col >= 0) {
        if (board[row][col] == 'Q')
          return false;
        col--;
      }

      row = duprow;
      col = dupcol;
      while (row < n && col >= 0) {
        if (board[row][col] == 'Q')
          return false;
        row++;
        col--;
      }
      return true;
    }

  public:
    void solve(int col, vector < string > & board, vector < vector < string >> & ans, int n) {
      if (col == n) {
        ans.push_back(board);
        return;
      }
      for (int row = 0; row < n; row++) {
        if (isSafe1(row, col, board, n)) {
          board[row][col] = 'Q';
          solve(col + 1, board, ans, n);
          board[row][col] = '.';
        }
      }
    }

  public:
    vector < vector < string >> solveNQueens(int n) {
      vector < vector < string >> ans;
      vector < string > board(n);
      string s(n, '.');
      for (int i = 0; i < n; i++) {
        board[i] = s;
      }
      solve(0, board, ans, n);
      return ans;
    }*/