# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
#
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rotten = {(i,j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i,j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        time = 0
        while fresh:
            if not rotten:
                return -1
            rotten = {(i+di, j+dj) for i, j in rotten for di,dj in [(0,1),(1,0),(0,-1),(-1,0)] if (i+di,j+dj) in fresh}
            fresh -= rotten
            time +=1
        return time