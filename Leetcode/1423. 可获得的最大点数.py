# 几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
#
# 每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
#
# 你的点数就是你拿到手中的所有卡牌的点数之和。
#
# 给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

def maxScore(cardPoints, k):
    n = len(cardPoints)
    total_sum = sum(cardPoints)

    # 如果 k 等于 n，直接返回总和
    if k == n:
        return total_sum

    # 初始化窗口大小为 n - k
    window_size = n - k
    window_sum = sum(cardPoints[:window_size])
    min_window_sum = window_sum

    # 滑动窗口
    for i in range(window_size, n):
        window_sum += cardPoints[i] - cardPoints[i - window_size]
        min_window_sum = min(min_window_sum, window_sum)

    # 返回结果
    return total_sum - min_window_sum


# 示例
cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(maxScore(cardPoints, k))  # 输出应为 12