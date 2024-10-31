# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
from typing import List
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = collections.Counter(nums)
        # return [item[0] for item in count.most_common(k)]
        count = collections.Counter(nums)
        heap = [(val, key) for key, val in count.items()]
        return [item[1] for item in heapq.nlargest(k, heap)]

if __name__ =='__main__':
    solution = Solution()
    nums = [1,1,1,2,2,3,3,3,3]
    k = 2
    print(solution.topKFrequent(nums, k))  # 输出应为 [1, 2]
