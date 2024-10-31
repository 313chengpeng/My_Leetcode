# 明明生成了
# N
# N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
#
# 数据范围：
# 1
# ≤
# n
# ≤
# 1000
#
# 1≤n≤1000  ，输入的数字大小满足
# 1
# ≤
# v
# a
# l
# ≤
# 500
#
# 1≤val≤500

def process_numbers(n, numbers):
    # 使用 set 去除重复的数字
    unique_numbers = set(numbers)

    # 对数字进行排序
    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers


def main():


    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    n = int(data[0])
    numbers = list(map(int, data[1:n + 1]))

    sorted_unique_numbers = process_numbers(n, numbers)

    for number in sorted_unique_numbers:
        print(number)


if __name__ == "__main__":
    main()