# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            if i < 0 or i>=m or j < 0 or j>=n or grid[i][j] != "1":
                return
            grid[i][j] = "2"
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)
        ans = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "1":
                    dfs(i,j)
                    ans += 1
        return ans