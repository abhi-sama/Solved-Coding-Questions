# Psuedocode:-
# 1)Create two array grids for bothe Pacific amnd Atlantic ocean.
# 2)Now straing from each boundaries of ocean see do a dfs traversal if it can be reached to the other side of ocean boundaries, if it can be reached marked that place as reachable by "True" otherwise "False" for each grid.
# 3)After both the traversal is completed for both of them , if a particular grid index is reachabel from both of them then it means the rain water can be reached from the particular coordinate to both the oceans.
# TC=O(m*n)
# SC=O(m*n)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pac_grid=[[False]*n for _ in range(m)]
        atl_grid=[[False]*n for _ in range(m)]
        res=[]
        q_pac=deque()
        q_atl=deque()
        for row in range(m):
            for col in range(n):
                if row==0 or col==0:
                    q_pac.append((row,col))
                if row==m-1 or col==n-1:
                    q_atl.append((row,col))
        
        def bfs(q,grid):
            dir=[[1,0],[-1,0],[0,-1],[0,1]]
            while q:
                row,col =q.pop()
                grid[row][col]=True
                for r,c in dir:
                    nrow=row+r
                    ncol=col+c
                    if nrow  in range(0,m) and ncol  in range(0,n) and heights[nrow][ncol] >= heights[row][col] and \
                    grid[nrow][ncol]==False:
                        q.append((nrow,ncol))


        bfs(q_pac,pac_grid)   
        bfs(q_atl,atl_grid)   
        
        for r in range(m):
            for c in range(n):
                if pac_grid[r][c] and atl_grid[r][c]:
                    res.append([r,c])
        
        return res

# TC=O(m*n)
# SC=O(m*n)
                    