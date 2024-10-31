# 写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
def hex_to_decimal(hex_str):
    # 使用 int 函数将十六进制字符串转换为十进制整数
    decimal_value = int(hex_str, 16)
    return str(decimal_value)


def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split("\n")

    results = []
    for hex_str in data:
        decimal_str = hex_to_decimal(hex_str)
        results.append(decimal_str)

    print("\n".join(results))


if __name__ == "__main__":
    main()
