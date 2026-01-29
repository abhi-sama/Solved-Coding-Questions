class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS=len(grid),len(grid[0])
        directions=[[-1,0],[0,1],[0,-1],[1,0]]
        def bfs():
            q=deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c]==0:
                        q.append(((r,c),0))

            while q:
                (row,col),dist=q.popleft()
                for dr,dc in directions:
                    nrow,ncol=row+dr,col+dc
                    if nrow in range(0,ROWS) and ncol in range(0,COLS) and \
                    dist+1<grid[nrow][ncol] and grid[nrow][ncol]!=-1:
                        grid[nrow][ncol]=dist+1
                        q.append(((nrow,ncol),dist+1))
        
        bfs()
        return 

# TC=O(m*n)       
# SC=O(m*n) 