class Solution:
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
        if col == n:
            ans.append(board[:])
            return
        
        for row in range(n):
            if leftrow[row] == 0 and lowerDiagonal[row+col] == 0 and upperDiagonal[n-1+col-row] == 0:
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                leftrow[row] = 1
                lowerDiagonal[row+col] = 1
                upperDiagonal[n-1+col-row] = 1
                self.solve(col+1, board, ans, leftrow,
                           upperDiagonal, lowerDiagonal, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                leftrow[row] = 0
                lowerDiagonal[row+col] = 0
                upperDiagonal[n-1+col-row] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ['.'*n for _ in range(n)]
        leftrow = [0]*n
        upperDiagonal = [0]*(2*n-1)
        lowerDiagonal = [0]*(2*n-1)
        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans

if __name__ == '__main__':
    n = 4
    obj = Solution()
    ans = obj.solveNQueens(n)
    for i in range(len(ans)):
        print("Arrangement", i+1)
        for j in range(len(ans[0])):
            print(ans[i][j])
            print()