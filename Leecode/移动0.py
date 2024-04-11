# 283
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

        # 将 left 指针之后的所有元素置为 0
        for i in range(left, len(nums)):
            nums[i] = 0