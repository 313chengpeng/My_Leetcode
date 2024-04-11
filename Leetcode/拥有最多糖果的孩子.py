# 1431.拥有最多糖果的孩子
# 给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。
#
# 对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有 最多 的糖果数目。

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_num = max(candies)
        pro = [candy + extraCandies >= max_num for candy in candies]
        return pro

if __name__ == '__main__':
    a = Solution()
    b = a.kidsWithCandies([2,3,5,1,3], 3)
    c = a.kidsWithCandies([4,2,1,1,2], 1)
    d = a.kidsWithCandies([12,1,12], 10)
    print(f"b={b},\n c={c},\n d={d}")
