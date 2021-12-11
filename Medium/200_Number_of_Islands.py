class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfs(grid, i, j):
                    count += 1
        return count
    
    # return the size of island from grid[i][j]
    def dfs(self, grid, i, j):
        count = 0
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1:
            return count
        if grid[i][j] == '0':
            return count
        if grid[i][j] == '!':
            return count
        else:
            # mark any grid[i][j] == 1 as visited
            grid[i][j] = '!'
            count += 1
            count += (self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1))
            return count
