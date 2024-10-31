# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))
                return
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]

        res = []
        dfs(0)
        return res
