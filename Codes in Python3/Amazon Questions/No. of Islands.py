class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        def bfs(r, c):
            q = deque()
            vis.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc
                    if (
                        0 <= nrow < rows
                        and 0 <= ncol < cols
                        and grid[nrow][ncol] == "1"
                        and (nrow, ncol) not in vis
                    ):
                        vis.add((nrow, ncol))
                        q.append((nrow, ncol))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in vis:
                    bfs(r, c)
                    islands += 1
        return islands
