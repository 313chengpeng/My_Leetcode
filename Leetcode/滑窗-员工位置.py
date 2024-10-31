# 题目描述：
# 工位由序列F1,F2...Fn 组成，Fi 值为0、1 或2。其中0 代表空置，1 代表有人，2 代表障碍
# 物。
# 1、某一空位的友好度为左右连续老员工数之和
# 2、为方便新员工学习求助，优先安排友好度高的空位
# 给出工位序列，求所有空位中友好度的最大值。
# 输入描述：
# 第一行为工位序列：F1,F2...Fn 组成，1<=n<=100000，Fi 值为0、1 或2。其中0 代表空置，1
# 代码有人，2 代表障碍物
# 其中0 代表空置，1 代码有人，2 代表障碍物。

def max_friendliness(workspaces):
    n = len(workspaces)

    # 初始化前缀和数组
    left_sum = [0] * n
    right_sum = [0] * n

    # 计算 left_sum
    for i in range(n):
        if workspaces[i] == 1:
            left_sum[i] = (left_sum[i - 1] + 1) if i > 0 else 1
        else:
            left_sum[i] = 0

    # 计算 right_sum
    for i in range(n - 1, -1, -1):
        if workspaces[i] == 1:
            right_sum[i] = (right_sum[i + 1] + 1) if i < n - 1 else 1
        else:
            right_sum[i] = 0

    # 计算每个空位的友好度，并记录最大值
    max_friendliness = 0
    for i in range(n):
        if workspaces[i] == 0:
            max_friendliness = max(max_friendliness, left_sum[i] + right_sum[i])

    return max_friendliness


# 示例
workspaces = [1, 1, 0, 2, 1, 0, 1, 1, 0, 2, 1]
print(max_friendliness(workspaces))  # 输出应为 4