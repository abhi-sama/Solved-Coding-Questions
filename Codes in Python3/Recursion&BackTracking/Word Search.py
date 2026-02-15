#Without Visited Array
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[[-1,0],[0,-1],[1,0],[0,1]]
        ROWS,COLS=len(board),len(board[0])

        def dfs(i,j,k):
            if k==len(word):
                return True
            if i not in range(ROWS) or j not in range(COLS):
                return False
            temp=board[i][j]
            board[i][j] = '#'

            for dr,dc in directions:
                nrow=dr+i
                ncol=dc+j
                if (nrow in range(ROWS)) and (ncol in range(COLS)) and board[nrow][ncol]==word[k]:
                    if dfs(nrow,ncol,k+1):
                        return True
            board[i][j] = temp
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]==word[0]:
                    if dfs(i,j,1):
                        return True
        return False
# N= m*n, board size
# for a word of lenght L we can only onlygo four directions but since 
# we are already coming from one direction it should be only 3 derctiond

# TC=O(N*3^L)
# SC=O(L)

#With Visited Array
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[[-1,0],[0,-1],[1,0],[0,1]]
        ROWS,COLS=len(board),len(board[0])

        def dfs(i,j,k,visit):
            if k==len(word):
                return True
            if i not in range(ROWS) or j not in range(COLS):
                return False

            visit.add((i,j))

            for dr,dc in directions:
                nrow=dr+i
                ncol=dc+j
                if (nrow in range(ROWS)) and (ncol in range(COLS)) and (nrow,ncol) not in visit and board[nrow][ncol]==word[k]:
                    if dfs(nrow,ncol,k+1,visit):
                        return True
            visit.remove((i,j))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]==word[0]:
                    if dfs(i,j,1,set()):
                        return True
        return False
# N= m*n, board size
# for a word of lenght L we can only onlygo four directions but since 
# we are already coming from one direction it should be only 3 derctiond

# TC=O(N*3^L)
# SC=O(L)