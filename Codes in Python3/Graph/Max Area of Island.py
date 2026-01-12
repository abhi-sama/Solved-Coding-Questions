#Solution 2
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        directions=[[-1,0],[0,1],[1,0],[0,-1]]
        visited=set()
        maxArea=0

        def dfs(r,c)->int:
            if( r not in range(ROWS) or c not in range(COLS) or grid[r][c]==0 or (r, c) in visited) :
                return 0
            visited.add((r,c))
            area=1
            for dr,dc in directions:
                area+=dfs(dr+r,dc+c)
            return area

        def bfs(r,c)->int:
            q=deque()
            visited.add((r,c))
            q.append((r,c))
            area=1
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nrow,ncol=dr+row,dc+col
                    if( nrow not in range(ROWS) or ncol not in range(COLS) or grid[nrow][ncol]==0 or (nrow, ncol) in visited):
                        continue
                    area+=1
                    visited.add((nrow,ncol))
                    q.append((nrow,ncol))
            return area    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    maxArea=max(maxArea,bfs(r,c))
        
        return maxArea

        

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         ROWS,COLS=len(grid), len(grid[0])
#         visit=set()
#         directions=[[-1,0],[0,1],[1,0],[0,-1]]
#         max_area=0

#         def dfs(r,c):
#             # if(r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]==0 or ):
#             #     return 0
#             area=1
#             visit.add((r,c))
#             for dr,dc in directions:
#                 nrow,ncol=dr+r,dc+c
#                 if(nrow in range(ROWS) and ncol in range(COLS)\
#                  and grid[nrow][ncol]==1 \
#                   and (nrow,ncol) not in visit ):
#                     area+=dfs(nrow,ncol)
#             return area


#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c]==1 and (r,c) not in visit:
#                     max_area=max(max_area, dfs(r,c) )

#         return max_area
