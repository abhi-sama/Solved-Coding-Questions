class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        vis=[[0]*n for _ in range(m)]
        q=[]
        fresh_count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append(((i,j),0))
                    vis[i][j]=1
                if grid[i][j]==1:
                    fresh_count+=1
        tm=0
        dr=[-1,0,+1,0]
        dc=[0,+1,0,-1]
        cnt=0
        while q:
            rc,t=q.pop(0)
            r,c=rc
            tm=max(tm,t)
            for i in range(4):
                nrow=r+dr[i]
                ncol=c+dc[i]
                if 0<=nrow<m and 0<=ncol<n and grid[nrow][ncol]==1 and vis[nrow][ncol]==0:
                    q.append(((nrow,ncol),t+1))
                    vis[nrow][ncol]=1
                    cnt+=1
        if cnt!=fresh_count:
            return -1
        return tm