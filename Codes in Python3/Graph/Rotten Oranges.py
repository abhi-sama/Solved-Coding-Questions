"""
Psuedocode:
1)Count all the rooten fresh fruit, while doing this also put created the visited set
for all the all the places where ther is an empty cell and also put all the rotten fruit in 
a queue including t=0 to show time 0.
2)While the queue is not empty start visiting in all the 4 directions and also put the time(depth) 
for each fresh fruit.Simulteanously reduce the fresh fruit count. 
3)After all the fruits are visited if the count of it equal to zero return the minmum time 
otherwise return -1.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        vis=set()
        ROWS,COLS=len(grid),len(grid[0])
        freshCnt=0
        minTime=0
        directions=[[-1,0],[0,1],[0,-1],[1,0]]
        q=deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    vis.add((r,c))
                elif grid[r][c]==1:
                    freshCnt+=1
                else:
                    q.append(((r,c),0))
                    vis.add((r,c))
        
        while q:
            (row,col),tm=q.popleft()
            minTime=max(tm,minTime)
            for dr,dc in directions:
                nrow,ncol=dr+row,dc+col
                if nrow in range(ROWS) and ncol in range(COLS) and (nrow,ncol) not in vis:
                    q.append(((nrow,ncol),tm+1))
                    vis.add((nrow,ncol))
                    freshCnt-=1

        return minTime if freshCnt==0 else -1

# TC=O(mn)
# SC=O(mn)