class Solution:
    def solve(self,row,col,s,m,ans,vis,di,dj,n):
        if row==(n-1) and col==(n-1):
            ans.append(s)
            return 
        dir="DLRU"
        for ind in range(4):
            nexti=row+di[ind]
            nextj=col+dj[ind]
            if 0<=nexti<n and 0<=nextj<n and m[nexti][nextj]==1 and vis[nexti][nextj]==0:
                vis[row][col]=1
                self.solve(nexti,nextj,s+dir[ind],m,ans,vis,di,dj,n)
                vis[row][col]=0
    def findPath(self, m, n):
        ans=[]
        vis=[[0]*n for _ in range(n)]
        di=[1,0,0,-1]
        dj=[0,-1,1,0]
        if m[0][0]:
            self.solve(0,0,"",m,ans,vis,di,dj,n)
        return ans