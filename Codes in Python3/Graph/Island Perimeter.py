# /*
# Psuedocode:-
# 1)Create a visited array grid.
# 2)Traverse the entire grid using DFS starting from a land position available in the grid in all the four direction.
# 3)If traversing in any one of the direction you find the grid boundary or water add a value 1 to the global perimeter variable.
# */
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        directions=[[-1,0],[0,1],[1,0],[0,-1]]
        perimeter=0

        def dfs(i,j):
            if(i not in range(rows) or j not in range(cols) or grid[i][j]==0):
               return 1  
            if((i,j) in visit):
                return 0  
            visit.add((i,j))
            peri=0
            for dr,dc in directions:
                nrow=i+dr
                ncol=j+dc
                peri= peri+dfs(nrow,ncol)
            
            return peri

        for row in range(rows):
            for col in range(cols):
                if(grid[row][col]==1 and (row,col) not in visit):
                    perimeter+=dfs(row,col)
        
        return perimeter
