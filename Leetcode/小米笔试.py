# 查找子字符串
# 对于子字符串s，查找是否存在子串t，如果存在子串t，将删除第一个子串t，并在字符串结尾添加一个字符串p。如果不存在子串t则认为字符串s已经规范化。循环进行规范化处理，直至字符串s已经规范化。若永远不能规范化则输出-1。
#输入描述，第一行第一个数T，表示组数。对于每组数据，第一行表示一个字符串s，第二行表示字符串t，第三行表示字符串p

# def normalize_string(s, t, p):
#     while t in s:
#         s = s.replace(t, '', 1) + p
#     return s
#
#
# def process_test_cases(T, test_cases):
#     results = []
#     for i in range(T):
#         s, t, p = test_cases[i]
#         original_s = s
#         seen_states = set()
#
#         while s not in seen_states:
#             if t not in s:
#                 results.append(s)
#                 break
#             seen_states.add(s)
#             s = s.replace(t, '', 1) + p
#             if t == p:
#                 results.append(-1)
#                 break
#             if len(s) > 10000:  # 防止无限循环，假设字符串长度超过10000时认为无法规范化
#                 results.append(-1)
#                 break
#
#         if len(results) <= i:
#             results.append(-1)
#
#     return results
#
#
# if __name__ == "__main__":
#     T = int(input().strip())
#     test_cases = []
#     for _ in range(T):
#         s = input().strip()
#         t = input().strip()
#         p = input().strip()
#         test_cases.append((s, t, p))
#
#     results = process_test_cases(T, test_cases)
#
#     for result in results:
#         print(result)

# 填字游戏
# 给定3*3的方格，要求把1~9不重不漏的填入这些方格，要求每个数字周围没有临近数，给出所有可能方案个数，如果没有任何可能的方案，则输出0。
# 输入：第一行的第一个数表示数据的组数。对每组数据，有三行，每行三个整数。a_ij表示表示第i行第j列。
def is_valid(grid, row, col, num):
    # 检查当前数字是否与周围的数字相邻
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3 and abs(grid[r][c] - num) == 1:
            return False
    return True


def solve(grid, pos, used, count):
    if pos == 9:
        count[0] += 1
        return

    row, col = divmod(pos, 3)
    if grid[row][col] != 0:
        if is_valid(grid, row, col, grid[row][col]):
            solve(grid, pos + 1, used, count)
    else:
        for num in range(1, 10):
            if not used[num] and is_valid(grid, row, col, num):
                grid[row][col] = num
                used[num] = True
                solve(grid, pos + 1, used, count)
                used[num] = False
                grid[row][col] = 0


def count_solutions(grid):
    count = [0]
    used = [False] * 10
    for num in range(1, 10):
        if grid[0][0] == num:
            used[num] = True
    solve(grid, 0, used, count)
    return count[0]


if __name__ == "__main__":
    T = int(input().strip())
    results = []
    for _ in range(T):
        grid = []
        for _ in range(3):
            row = list(map(int, input().strip().split()))
            grid.append(row)
        result = count_solutions(grid)
        results.append(result)

    for result in results:
        print(result)