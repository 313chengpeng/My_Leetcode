# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
import random
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def quicksort(nums, k):
            provat = random.choice(nums)
            big = []
            small = []
            equal = []
            for num in nums:
                if num > provat:
                    big.append(num)
                elif num < provat:
                    small.append(num)
                else:
                    equal.append(num)
            if len(big) == k - 1 or (len(big) < k - 1 and len(equal) + len(big) >= k):
                return provat
            if len(big) < k - 1:
                return quicksort(small + equal, k - len(big))
            if len(big) > k - 1:
                return quicksort(big, k)

        return quicksort(nums, k)

# 使用堆排序
import heapq
class Solution_heapq:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

if __name__ == '__main__':
    a = Solution_heapq()
    print(a.findKthLargest([3,2,1,5,6,4], 2))
    print(a.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
