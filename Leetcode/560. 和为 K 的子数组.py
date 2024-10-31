# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。
from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 初始化前缀和数组
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x

        # 使用哈希表记录前缀和出现的次数
        cnt = defaultdict(int)
        ans = 0

        # 遍历前缀和数组
        for sj in s:
            # 如果存在前缀和 sj - k，则说明存在子数组和为 k
            ans += cnt[sj - k]
            # 记录当前前缀和出现的次数
            cnt[sj] += 1

        return ans


# 测试
if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,-1,1,-1]
    k = 1
    print(solution.subarraySum(nums, k))  # 输出应为 2