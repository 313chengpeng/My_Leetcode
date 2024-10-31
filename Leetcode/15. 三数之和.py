# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 对于长度小于3或者null的数组之间返回[]
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        res=[]
        nums.sort()
        for i in range(n):
            if(nums[i]>0):  # 当nums[i]>0时说明，后面已经找不到和等于0的三元组
                return res
            if(i>0 and nums[i]==nums[i-1]): # 避免重复值
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(nums))