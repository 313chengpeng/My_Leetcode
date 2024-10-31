# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长
# 子串的长度。
# 参考网址
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res


if __name__ == '__main__':
    s = "pwwkewdsaodhjsakldasidlasjioldjas"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(solution.lengthOfLongestSubstring(s))
