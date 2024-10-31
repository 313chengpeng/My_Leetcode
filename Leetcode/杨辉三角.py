# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# def generate(num_rows):
#     if num_rows == 0:
#         return []
#
#     triangle = []
#     for row_num in range(num_rows):
#         # 创建当前行，并用1填充
#         row = [1] * (row_num + 1)
#         # 计算非边界元素
#         for j in range(1, row_num):
#             row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
#         # 添加当前行到三角形
#         triangle.append(row)
#
#     return triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = [[1]* (i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1,i):
                c[i][j]=c[i-1][j-1]+c[i-1][j]
        return c


# 示例
print(generate(5))