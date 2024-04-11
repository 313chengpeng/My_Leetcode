# 1679

# 给你一个整数数组 nums 和一个整数 k 。
#
# 每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。
#
# 返回你可以对数组执行的最大操作数

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
          # 记录每个元素出现的次数
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        operations = 0

        for num in nums:
            complement = k - num
            if complement != num :
                if num_counts.get(complement, 0) > 0 and num_counts[num]>0:
                    operations += 1
                    # 减少 num 和其 complement 在哈希表中的出现次数
                    num_counts[num] -= 1
                    num_counts[complement] -= 1
            else:
                if num_counts.get(complement, 0) > 1:
                    operations += 1
                    # 减少 num 和其 complement 在哈希表中的出现次数
                    num_counts[num] -= 1
                    num_counts[complement] -= 1

        return operations
