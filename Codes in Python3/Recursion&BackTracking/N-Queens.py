#Backtracking using Hashset
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board = [["."] * n for i in range(n)]
        col=set()
        posDiag=set()
        negDiag=set()

        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add((r+c))
                negDiag.add((r-c))
                board[r][c]="Q"
                backtrack(r+1)
                board[r][c]="."
                negDiag.remove((r-c))
                posDiag.remove((r+c))
                col.remove(c)

        backtrack(0)
        return res
# TC=O(n!)
# SC=O(n^2)


#Backtracking
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board = [["."] * n for i in range(n)]

        def isSafe(r,c):
            row=r-1
            while row>=0:
                if board[row][c]=="Q":
                    return False
                row-=1
            
            row,col=r-1,c-1
            while row>=0 and col>=0:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1
            
            row,col=r-1,c+1
            while row>=0 and col<n:
                if board[row][col]=="Q":
                    return False
                row-=1
                col+=1
            return True          

        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if isSafe(r,c):
                    board[r][c]="Q"
                    backtrack(r+1)
                    board[r][c]="."

        backtrack(0)
        return res
# TC=O(n!)
# SC=O(n^2)
