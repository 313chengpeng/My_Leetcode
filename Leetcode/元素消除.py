def find_best_start(nums, interval):
    # 创建一个字典来记录每个起点及其能够消除的元素数量
    count_dict = {}

    # 遍历数组中的每个元素，作为起点
    for start in nums:
        count = 0
        current = start
        while current in nums:
            count += 1
            current += interval

        # 记录起点及其对应的消除元素数量
        count_dict[start] = count

    # 找到消除元素最多的起点
    max_count = 0
    best_start = float('inf')
    for start, count in count_dict.items():
        if count > max_count or (count == max_count and start < best_start):
            max_count = count
            best_start = start

    return best_start


# 示例
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
interval = 3
print(find_best_start(nums, interval))  # 输出应为 1