class Solution:
    def bfs(self,srow,scol,vis,grid):
        vis[srow][scol]=True
        q=[(srow,scol)]
        m=len(grid)
        n=len(grid[0])
        while q:
            row,col=q.pop()
            for delrow in range(-1,2):
                for delcol in range(-1,2):
                    nrow=row+delrow
                    ncol=col+delcol
                    if(nrow>=0 and nrow<m and 
                    ncol>=0 and ncol<n and
                    grid[nrow][ncol]==1 and 
                    vis[nrow][ncol] is False):
                        vis[nrow][ncol]=True
                        q.append((nrow,ncol))
                    
    def numIslands(self,grid):
        m=len(grid)
        n=len(grid[0])
        vis=[[False]*n for _ in range(m)]
        count=0
        for row in range(m):
            for col in range(n):
                if vis[row][col] is False and grid[row][col]==1:
                    count+=1
                    self.bfs(row,col,vis,grid)
        return count