def nearest(mat,n,m):
    vis=[[0]*m for _ in range(n)]
    dis=[[0]*m for _ in range(n)]
    q=[]
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:
                q.append((i,j,0))
                vis[i][j]=1
            
    while q:
        row,col,step=q.pop(0)
        dr=[-1,0,+1,0]
        dc=[0,+1,0,-1]
        dis[row][col]=step
        for i in range(4):
            nrow=row+dr[i]
            ncol=col+dc[i]
            if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]==0:
                vis[nrow][ncol]=1
                q.append((nrow,ncol,step+1))
    return dis
    pass
