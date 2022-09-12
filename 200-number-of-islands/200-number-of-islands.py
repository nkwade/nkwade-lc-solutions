class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited or grid[r][c] == '0':
                return
            
            visited.add((r,c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for row_dir, col_dir in directions:
                new_r = r + row_dir
                new_c = c + col_dir
                dfs(new_r, new_c)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        return islands