# 51. N 皇后 - 回溯算法.py
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        m = n * 2 - 1
        ans = []
        col = [0] * n
        on_path, diag1, diag2 = [False] * n, [False] * m, [False] * m
        def dfs(r: int) -> None:
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c)  for c in col])
                return
            for c, on in enumerate(on_path):
                if not on and not diag1[r + c] and not diag2[r - c]:
                    col[r] = c
                    on_path[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
        dfs(0)
        return ans


# 问题概述
# N皇后问题要求在一个 N×N 的棋盘上放置 N 个皇后，使得任何两个皇后都不能在同一行、同一列或同一对角线上。
#
# 代码解释
# 初始化：
#
# m = n * 2 - 1：表示可能的对角线的总数。
# ans = []：用于存储所有可能的解决方案。
# col = [0] * n：用于存储每一行皇后所在的列。
# on_path, diag1, diag2：这些是布尔列表，用于跟踪已经被皇后占据的列和对角线。
# on_path：跟踪每一列是否被占用。
# diag1：跟踪从左上到右下的主对角线。
# diag2：跟踪从右上到左下的副对角线。
# 深度优先搜索 (DFS) 函数：
#
# def dfs(r: int) -> None：一个辅助函数，尝试逐行放置皇后。
# 基准情况：如果 r == n，说明所有皇后都成功放置，将当前棋盘配置添加到 ans。
# 遍历列：对于当前行 r 中的每一列 c：
# 检查约束：确保当前列 c、主对角线 r + c 和副对角线 r - c 没有被占用。
# 放置皇后：如果合法，更新 col、on_path、diag1 和 diag2 来标记皇后的位置。
# 递归到下一行：调用 dfs(r + 1) 在下一行放置皇后。
# 回溯：在递归调用后，重置状态（on_path、diag1 和 diag2），以探索其他配置。
# 返回结果：
#
# dfs(0)：从第一行开始进行深度优先搜索。
# return ans：返回所有合法的棋盘配置。


if __name__ == '__main__':
    a = Solution()
    b = a.solveNQueens(4)
    print(b)

