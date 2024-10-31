# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组
# 是数组中的一个连续部分。

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        a = max(nums)
        lmax = 0
        gmax = 0
        if a < 0:
            return a
        else :
            for num in nums:
                lmax = max(0, lmax+num)
                gmax = max(gmax, lmax)
            return gmax

if __name__ == '__main__':
    a = Solution()
    print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(a.maxSubArray([1]))
    print(a.maxSubArray([5,4,-1,7,8]))
    print(a.maxSubArray([-1]))