def max_conferences(n, k, intervals):
    # 按结束时间升序排序，如果结束时间相同则按开始时间升序排序
    intervals.sort(key=lambda x: (x[1], x[0]))

    # 记录每一天已经参加的博览会数量
    day_participation = {}

    # 记录参加的博览会总数
    total_conferences = 0

    for start, end in intervals:
        for day in range(start, end + 1):
            if day not in day_participation:
                day_participation[day] = 0

            if day_participation[day] < k:
                # 参加这场博览会
                day_participation[day] += 1
                total_conferences += 1
                break  # 参加完这场博览会后，跳出循环，考虑下一个博览会

    return total_conferences


# 示例
n = 5
k = 2
intervals = [(1, 2), (2, 3), (3, 4), (1, 3), (2, 4)]
print(max_conferences(n, k, intervals))  # 输出应为 4