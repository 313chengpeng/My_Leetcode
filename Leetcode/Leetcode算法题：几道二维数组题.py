# 一、对角线遍历

def find_diagonal_order(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []
    # 初始方向设置为向上
    going_up = True
    for sum_ in range(rows + cols - 1):
        if going_up:
            # 当方向向上时，从左下到右上
            x = min(sum_, rows - 1)
            y = sum_ - x
            while x >= 0 and y < cols:
                result.append(matrix[x][y])
                x -= 1
                y += 1
        else:
            # 当方向向下时，从右上到左下
            y = min(sum_, cols - 1)
            x = sum_ - y
            while y >= 0 and x < rows:
                result.append(matrix[x][y])
                x += 1
                y -= 1
        # 每次遍历完一条对角线后改变方向
        going_up = not going_up

    return result


# 示例
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(find_diagonal_order(matrix))
