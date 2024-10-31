# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。


# 每次循环不再只将指针移动一格（i++），而是不断移动指针（while循环），直到找到比先前的短板高度更高的地方再停止，再计算面积。
#
# 因为在移动短板指针的过程中，宽度已经在不断减少了，如果短板更短了，面积一定更小。所以这种情况我们可以省去，不用计算讨论。我们期望的是能找到比之前的短板更高的板，这样面积才有可能提高

# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         l,r = 0, len(height) - 1
#         ans = 0
#         while l < r:
#             area = min(height[l],height[r])*(r-l)
#             ans = max(ans,area)
#             if height[l] <= height[r]:
#                 l += 1
#             else:
#                 r = r-1
#         return ans

class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height)-1
        max_value = 0
        while i != j:
            if height[i] < height[j]:
                max_value = max(max_value, height[i]*(j-i))
                # temp = height[i]
                i += 1
                # while height[i] <= temp:
                #     i += 1
            else:
                max_value = max(max_value, height[j]*(j-i))
                # temp = height[j]
                j -= 1
                # while height[j] <= temp and j != i:
                #     j -= 1
        return max_value
if __name__ == '__main__':
    a = Solution()
    b = a.maxArea([1,8,6,2,5,4,8,3,7])
    print(b)