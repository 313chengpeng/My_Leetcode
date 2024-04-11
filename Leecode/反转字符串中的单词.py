# 151
# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。
#
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
#
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
#
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

class Solution:
    def reverseWords(self, s: str) -> str:
        # 去除前后空格，按照空格分割成单词列表
        words = s.strip().split()
        # 反转单词列表
        words.reverse()
        # 用单个空格连接单词列表，得到结果字符串
        return ' '.join(words)

if __name__ == '__main__':
    a = Solution()
    b = a.reverseWords("the sky is blue")
    c = a.reverseWords("  hello world  ")
    d = a.reverseWords("a good   example")
    print(f"b={b}, c={c}, d={d}")