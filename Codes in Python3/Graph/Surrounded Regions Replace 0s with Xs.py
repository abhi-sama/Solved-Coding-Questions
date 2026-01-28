class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        visited=[[False]*COLS for _ in range(ROWS)]
        direction=[[-1,0],[0,-1],[1,0],[0,1]]
        def dfs(r,c):
            if visited[r][c]:
                return
            visited[r][c]=True
            for dr,dc in direction:
                nrow,ncol=dr+r,dc+c
                if nrow in range(0,ROWS) and ncol in range(0,COLS) \
                and board[nrow][ncol]=="O" \
                and visited[nrow][ncol]==False:
                    dfs(nrow,ncol)
        
        for r in range(ROWS):
            if visited[r][0]==False and board[r][0]=="O":
                    dfs(r,0)
            if visited[r][COLS-1]==False and board[r][COLS-1]=="O":
                    dfs(r,COLS-1)           

        for c in range(COLS):
            if visited[0][c]==False and board[0][c]=="O":
                    dfs(0,c)
            if visited[ROWS-1][c]==False and board[ROWS-1][c]=="O":
                    dfs(ROWS-1,c)           
        
        for r in range(ROWS):
            for c in range(COLS):
                if visited[r][c]==False and board[r][c]=="O":
                    board[r][c]="X"

# TC=O(m*n)
# SC=O(m*n)