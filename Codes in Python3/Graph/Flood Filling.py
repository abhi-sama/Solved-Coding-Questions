class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        ans=image
        init_color=image[sr][sc]
        q=[]
        dr=[-1,0,+1,0]
        dc=[0,+1,0,-1]
        q.append((sr,sc))
        ans[sr][sc]=color
        while q:
            r,c=q.pop(0)
            image[r][c]=color
            for i in range(4):
                nrow=r+dr[i]
                ncol=c+dc[i]
                if 0<=nrow<m and 0<=ncol<n and image[nrow][ncol]==init_color and ans[nrow][ncol]!=color:
                    q.append((nrow,ncol))
                    
        return ans

