# 某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
# 小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
# 数据范围：输入的正整数满足
# 1
# ≤
# n
# ≤
# 100
#
# 1≤n≤100
#
# 注意：本题存在多组输入。输入的
# 0
# 表示输入结束，并不用输出结果。

def max_drink_bottles(n):
    total_drinks = 0  # 总共喝掉的汽水瓶数
    current_bottles = n  # 当前拥有的空瓶子数

    while current_bottles >= 3:
        # 每3个空瓶子可以换1瓶汽水
        drinks = current_bottles // 3
        total_drinks += drinks

        # 喝完汽水后产生的新空瓶子
        new_bottles = drinks

        # 剩余的空瓶子加上新产生的空瓶子
        current_bottles = current_bottles % 3 + new_bottles

        # 如果剩余2个空瓶子，可以向老板借1个空瓶子，再兑换1瓶汽水
        if current_bottles == 2:
            total_drinks += 1
            current_bottles = 1  # 喝完后归还借来的1个空瓶子，剩下1个空瓶子

    return total_drinks


def main():
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        print(max_drink_bottles(n))


if __name__ == "__main__":
    main()