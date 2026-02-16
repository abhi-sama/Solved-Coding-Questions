# Psuedocode:-
# 1) Create a minheap starting with inserting the (0,0) cordinate along
#    with intial absolute difference of zero.
# 2) Do bfs kind of traversal going in 4 directions 
# 3) Whenever you pop something from the heap check whether it is the maximum abs diff
# 4) Stop after cell had been visited.

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS,COLS=len(heights),len(heights[0])
        visit=set()
        minHeap=[(0,0,0)]
        maxDiff=0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff,i,j=heapq.heappop(minHeap)
            maxDiff=max(diff,maxDiff)
            if (i,j) in visit:
                continue
            if i==ROWS-1 and j==COLS-1:
                break
            visit.add((i,j))
            for dr,dc in directions:
                nrow=dr+i
                ncol=dc+j
                if nrow in range(ROWS) and ncol in range(COLS) and (nrow,ncol) not in visit:
                    heapq.heappush(minHeap,(abs(heights[nrow][ncol]-heights[i][j]),nrow,ncol))
        
        return maxDiff

# TC=O(m*n*log(mn))
# SC=O(m*n)
