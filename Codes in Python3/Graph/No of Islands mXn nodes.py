##Solution 5
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        visited=set()
        dir=[[-1,0],[0,1],[1,0],[0,-1]]
        nos_islands=0

        def dfs(i,j):
            if (i not in range(0,ROWS)) or (j not in range(0,COLS)) or (grid[i][j]=="0"):
                return 
            if (i,j) in visited:
                return
            visited.add((i,j))
            for dr,dc in dir:
                dfs(i+dr,j+dc)

        def bfs (r,c):
            q=deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row,col=q.popleft()
                for dr,dc in dir:
                    nrow,ncol=row+dr,col+dc
                    if (0 <= nrow < ROWS and 0 <= ncol < COLS and grid[nrow][ncol] == "1" and (nrow, ncol) not in visited):
                        q.append((nrow,ncol))
                        visited.add((nrow,ncol))


        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c]=="1" and (r,c) not in visited):
                    bfs(r,c)
                    nos_islands+=1 
        
        return   nos_islands

            



##Solution 1
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         rows, cols= len(grid), len(grid[0])
#         visit=set()
#         islands=0

#         def bfs(r,c):
#             q=collections.deque()
#             visit.add((r,c))
#             q.append((r,c))
#             while q:
#                 r,c = q.popleft()
#                 directions=[[-1,0],[0,1],[1,0],[0,-1]]
#                 for dr,dc in directions:
#                     nrow, ncol= r+dr, c+dc
#                     if(nrow in range(rows) and
#                        ncol in range(cols) and
#                        grid[nrow][ncol] == "1" and 
#                        (nrow,ncol) not in visit ):
#                        q.append((nrow,ncol))
#                        visit.add((nrow,ncol))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]=="1" and (r,c) not in visit:
#                     bfs(r,c)
#                     islands+=1
#         return islands
    
##Solution 2
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         ROWS,COLS = len(grid),len(grid[0])
#         directions=[[-1,0],[0,1],[1,0],[0,-1]]
#         island_count=0

#         def dfs(r,c):
#             if (r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]=="0"):
#                 return
#             grid[r][c]="0"
#             for dr, dc in directions:
#                 dfs(r+dr,c+dc)

#         def bfs(r,c):
#             q=deque()
#             grid[r][c]="0"
#             q.append((r,c))

#             while q:
#                 row,col= q.popleft()
#                 for dr,dc in directions:
#                     nrow, ncol= row + dr, col + dc
#                     if (nrow<0 or ncol<0 or nrow>=ROWS or ncol>=COLS or grid[nrow][ncol]=="0"):
#                         continue
#                     q.append((nrow,ncol))
#                     grid[nrow][ncol]="0"

        
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c]=="1":
#                     bfs(r,c)
#                     island_count+=1
        
#         return island_count

        


##Solution 3
# class Solution:
#     def bfs(self,srow,scol,vis,grid):
#         vis[srow][scol]=True
#         q=[(srow,scol)]
#         m=len(grid)
#         n=len(grid[0])
#         while q:
#             row,col=q.pop()
#             for delrow in range(-1,2):
#                 for delcol in range(-1,2):
#                     nrow=row+delrow
#                     ncol=col+delcol
#                     if(nrow>=0 and nrow<m and 
#                     ncol>=0 and ncol<n and
#                     grid[nrow][ncol]==1 and 
#                     vis[nrow][ncol] is False):
#                         vis[nrow][ncol]=True
#                         q.append((nrow,ncol))
                    
#     def numIslands(self,grid):
#         m=len(grid)
#         n=len(grid[0])
#         vis=[[False]*n for _ in range(m)]
#         count=0
#         for row in range(m):
#             for col in range(n):
#                 if vis[row][col] is False and grid[row][col]==1:
#                     count+=1
#                     self.bfs(row,col,vis,grid)
#         return count