def dfs(row,col,arr,vis,vec,m,n,row0,col0):
    vis[row][col]=1
    vec.append((row-row0,col-col0))
    delrow=[-1,0,+1,0]
    delcol=[0,+1,0,-1]
    for i in range(4):
        nrow= row+delrow[i]
        ncol= col+delcol[i]
        if (nrow>=0 and nrow<m and
         ncol>=0 and ncol<n and 
         vis[nrow][ncol]==0 and arr[nrow][ncol]==1):
            dfs(nrow,ncol,arr,vis,vec,m,n,row0,col0)

def distinctIsland(arr,m,n) :
    vis=[[0]*n for _ in range(m)]
    s=set()#declare set
    for i in range(m):
        for j in range(n):
            if vis[i][j]==0 and arr[i][j]==1:
                vec=[]
                dfs(i,j,arr,vis,vec,m,n,i,j)
                s.add(tuple(vec)) 
                 # convert the list to a tuple to make it hashable
    return len(s)            
