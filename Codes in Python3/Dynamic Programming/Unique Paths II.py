#Space Optimised Bottom Up Approach
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        next_row=[0]*(COLS+1)
        if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
            return 0
        next_row[COLS-1]=1
    
        for row in range(ROWS-1,-1,-1):
            curr_row=[0]*(COLS+1)
            for col in range(COLS-1,-1,-1):
                if grid[row][col] == 1:
                    curr_row[col] = 0
                else:    
                    right=curr_row[col+1]
                    down=next_row[col]
                    curr_row[col]+=right + down
            next_row=curr_row
        return next_row[0]

# TC=O(m*n)
# SC=O(n)

#Bottom Up Approach
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        dp=[[0]*(COLS+1) for _ in range(ROWS+1)]
        if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
            return 0
        dp[ROWS-1][COLS-1]=1
    
        for row in range(ROWS-1,-1,-1):
            for col in range(COLS-1,-1,-1):
                if grid[row][col] == 1:
                    dp[row][col] = 0
                else:    
                    right=dp[row][col+1]
                    down=dp[row+1][col]
                    dp[row][col]+=right + down

        return dp[0][0]

# TC=O(m*n)
# SC=O(m*n)
        

#Top Down Approach
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        dp=[[-1]*COLS for _ in range(ROWS)]
        if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
            return 0
        def f(row,col):
            if row==(ROWS-1) and col==(COLS-1):
                return 1
            if row not in range(ROWS) or col not in range(COLS) \
            or grid[row][col]==1:
                return 0
            if dp[row][col]!=-1:
                return dp[row][col]

            right=f(row,col+1)
            down=f(row+1,col)
            dp[row][col]=right + down
            return dp[row][col]

        return f(0,0)

# TC=O(m*n)
# SC=O(m*n)
        